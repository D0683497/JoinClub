using System;
using System.Collections.Generic;
using System.Security.Claims;
using System.Threading.Tasks;
using AutoMapper;
using JoinClub.Data;
using JoinClub.Entities.Application;
using JoinClub.Models.Account;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace JoinClub.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class AccountController : ControllerBase
    {
        private readonly ILogger<AccountController> _logger;
        private readonly UserManager<ApplicationUser> _userManager;
        private readonly IMapper _mapper;
        private readonly ApplicationDbContext _applicationDbContext;

        public AccountController(
            ILogger<AccountController> logger, 
            UserManager<ApplicationUser> userManager, 
            IMapper mapper, 
            ApplicationDbContext applicationDbContext)
        {
            _logger = logger;
            _userManager = userManager;
            _mapper = mapper;
            _applicationDbContext = applicationDbContext;
        }

        [AllowAnonymous]
        [HttpPost("register", Name = nameof(Register))]
        public async Task<IActionResult> Register(RegisterViewModel model)
        {
            var entity = _mapper.Map<ApplicationUser>(model);
            
            using (var scope = await _applicationDbContext.Database.BeginTransactionAsync())
            {
                try
                {
                    var createUserResult = await _userManager.CreateAsync(entity, model.Password);
                    if (createUserResult.Succeeded)
                    {
                        var currentUser = await _userManager.FindByNameAsync(entity.UserName);
                        _logger.LogInformation($"建立{currentUser.Id}成功");
                        var addRoleResult = await _userManager.AddToRoleAsync(currentUser, "Member");
                        if (addRoleResult.Succeeded)
                        {
                            _logger.LogInformation($"添加{currentUser.Id}角色成功");
                            var claims = new List<Claim>
                            {
                                new Claim(ClaimTypes.NameIdentifier, string.IsNullOrEmpty(currentUser.Id) ? "" : currentUser.Id),
                                new Claim(ClaimTypes.Name, string.IsNullOrEmpty(currentUser.UserName) ? "" : currentUser.UserName),
                                new Claim(ClaimTypes.Email, string.IsNullOrEmpty(currentUser.Email) ? "" : currentUser.Email),
                                new Claim(ClaimTypes.MobilePhone, string.IsNullOrEmpty(currentUser.PhoneNumber) ? "" : currentUser.PhoneNumber)
                            };
                            var addClaimResult = await _userManager.AddClaimsAsync(currentUser, claims);
                            if (addClaimResult.Succeeded)
                            {
                                _logger.LogInformation($"添加{currentUser.Id}聲明成功");
                                await scope.CommitAsync();
                                _logger.LogInformation($"註冊{currentUser.Id}成功");
                                return Ok();
                            }
                            _logger.LogError($"添加{currentUser.Id}聲明失敗");
                        }
                        _logger.LogError($"添加{currentUser.Id}角色失敗");
                    }
                    
                    _logger.LogWarning($"建立{entity.UserName}失敗");
                    await scope.RollbackAsync();
                    return BadRequest("註冊失敗");
                }
                catch (Exception e)
                {
                    _logger.LogError($"註冊{entity.UserName}失敗");
                    _logger.LogError($"{e.ToString()}");
                    throw;
                }
            }
        }
        
        [Authorize]
        [HttpPost("change-password", Name = nameof(ChangePassword))]
        public async Task<IActionResult> ChangePassword(ChangePasswordViewModel model)
        {
            var user = await _userManager.FindByIdAsync(model.UserId);

            if (user == null)
            {
                _logger.LogError($"{model.UserId}修改密碼，找不到使用者");
                return BadRequest();
            }

            var checkPasswordResult = await _userManager.CheckPasswordAsync(user, model.OldPassword);
            if (!checkPasswordResult)
            {
                _logger.LogWarning($"{user.Id}修改密碼，舊密碼錯誤");
                return BadRequest();
            }
            
            var changePasswordResult = await _userManager.ChangePasswordAsync(user, model.OldPassword, model.NewPassword);
            if (changePasswordResult.Succeeded)
            {
                _logger.LogInformation($"{user.Id}修改密碼成功");
                return Ok();
            }
            
            _logger.LogError($"{user.Id}修改密碼失敗");
            return BadRequest();
        }
    }
}