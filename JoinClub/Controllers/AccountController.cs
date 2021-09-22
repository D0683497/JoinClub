using System;
using System.Collections.Generic;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Text;
using System.Threading.Tasks;
using FluentValidation.Results;
using JoinClub.Dtos.Account;
using JoinClub.Entities.Identity;
using JoinClub.Validator.Account;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using Microsoft.IdentityModel.Tokens;

namespace JoinClub.Controllers
{
    [AllowAnonymous]
    [ApiController]
    [Route("api/[controller]")]
    public class AccountController : ControllerBase
    {
        private readonly ILogger<AccountController> _logger;
        private readonly UserManager<ApplicationUser> _userManager;
        private readonly SignInManager<ApplicationUser> _signInManager;
        private readonly IConfiguration _configuration;
        private readonly IWebHostEnvironment _environment;

        public AccountController(
            ILogger<AccountController> logger, 
            UserManager<ApplicationUser> userManager, 
            SignInManager<ApplicationUser> signInManager, 
            IConfiguration configuration, 
            IWebHostEnvironment environment)
        {
            _logger = logger;
            _userManager = userManager;
            _signInManager = signInManager;
            _configuration = configuration;
            _environment = environment;
        }

        /// <summary>
        /// 登入
        /// </summary>
        [AllowAnonymous]
        [HttpPost("login", Name = nameof(Login))]
        public async Task<ActionResult<LoginResponseDto>> Login([FromBody] LoginDto dto)
        {
            LoginDtoValidator validator = new LoginDtoValidator();
            ValidationResult result = await validator.ValidateAsync(dto);
            if (result.IsValid)
            {
                #region 檢查是否可登入

                var user = await _userManager.FindByNameAsync(dto.UserName);
                if (user == null)
                {
                    return Problem(title: "登入失敗", detail: "請檢查您的帳號密碼是否正確", statusCode: 403);
                }
                if (!user.EmailConfirmed)
                {
                    return Problem(title: "帳戶尚未驗證", detail: "請前往您的信箱收取驗證信", statusCode: 403);
                }
                if (!user.Enable)
                {
                    return Problem(title: "帳戶尚未啟用", detail: "請聯絡管理員", statusCode: 403);
                }

                #endregion
                
                #region 檢查密碼
                
                var checkPasswordResult = await _signInManager.CheckPasswordSignInAsync(user, dto.Password, true);
                if (checkPasswordResult.IsLockedOut)
                {
                    return Problem(title: "帳戶被鎖定", detail: "請聯絡管理員", statusCode: 403);
                }
                if (checkPasswordResult.IsNotAllowed)
                {
                    return Problem(title: "帳戶尚未驗證", detail: "請前往您的信箱收取驗證信", statusCode: 403);
                }
                if (checkPasswordResult.Succeeded)
                {
                    // TODO: 角色
                    
                    var claims = new List<Claim>
                    {
                        new Claim(ClaimTypes.NameIdentifier, user.Id),
                        new Claim(ClaimTypes.Name, user.UserName),
                        new Claim(ClaimTypes.Email, user.Email),
                        new Claim(ClaimTypes.Sid, user.SecurityStamp)
                    };
                    
                    var returnDto = new LoginResponseDto { Token = GenerateJwtToken(claims) };
                    return Ok(returnDto);
                }
                
                #endregion
                
                return Problem(title: "登入失敗", detail: "請檢查您的帳號密碼是否正確", statusCode: 403);
            }
            return BadRequest(result.Errors);
        }
        
        [NonAction]
        private string GenerateJwtToken(IList<Claim> claims)
        {
            claims.Add(new Claim(JwtRegisteredClaimNames.Jti, Guid.NewGuid().ToString()));
            
            var userClaimsIdentity = new ClaimsIdentity(claims);
            var securityKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(_configuration["JWT:Key"]));
            var signingCredentials = new SigningCredentials(securityKey, _environment.IsDevelopment() ? SecurityAlgorithms.HmacSha256 : SecurityAlgorithms.HmacSha256Signature);
            
            var tokenDescriptor = new SecurityTokenDescriptor
            {
                Issuer = _configuration["JWT:Issuer"],
                Audience = _configuration["JWT:Audience"],
                Subject = userClaimsIdentity,
                NotBefore = DateTime.UtcNow, // Token 在什麼時間之前，不可用
                IssuedAt = DateTime.UtcNow, // Token 的建立時間
                Expires = DateTime.Now.AddHours(8), // Token 的逾期時間
                SigningCredentials = signingCredentials
            };
            
            var tokenHandler = new JwtSecurityTokenHandler();
            var securityToken = tokenHandler.CreateToken(tokenDescriptor);
            var serializeToken = tokenHandler.WriteToken(securityToken);

            return serializeToken;
        }
    }
}
