using System.Collections.Generic;
using System.Security.Claims;
using System.Threading.Tasks;
using AutoMapper;
using JoinClub.Data;
using JoinClub.Entities.Application;
using JoinClub.Models.Account;
using JoinClub.Models.User;
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
            
            using (var transaction = _applicationDbContext.Database.BeginTransaction())
            {
                var createUserResult = await _userManager.CreateAsync(entity, model.Password);
                if (!createUserResult.Succeeded)
                {
                    await transaction.RollbackAsync();
                    _logger.LogError($"{model.UserName}建立失敗");
                    return BadRequest("註冊失敗");
                }
            
                var currentUser = await _userManager.FindByNameAsync(model.UserName);
                var claims = new List<Claim>
                {
                    new Claim(ClaimTypes.NameIdentifier, string.IsNullOrEmpty(currentUser.Id) ? "" : currentUser.Id),
                    new Claim(ClaimTypes.Name, string.IsNullOrEmpty(currentUser.UserName) ? "" : currentUser.UserName),
                };
                var addClaimResult = await _userManager.AddClaimsAsync(currentUser, claims);
                if (!addClaimResult.Succeeded)
                {
                    await transaction.RollbackAsync();
                    _logger.LogError($"{model.UserName}添加聲明");
                    return BadRequest("註冊失敗");
                }
                
                await transaction.CommitAsync();
                _logger.LogInformation($"{model.UserName}建立成功");
            }

            return Ok();
        }
        
        [Authorize]
        [HttpPost("{userId}/change-password", Name = nameof(ChangePassword))]
        public async Task<IActionResult> ChangePassword(string userId, ChangePasswordViewModel model)
        {
            var user = await _userManager.FindByIdAsync(userId);
            if (user == null)
            {
                _logger.LogError($"{userId}修改密碼，找不到使用者");
                return BadRequest();
            }

            var checkPasswordResult = await _userManager.CheckPasswordAsync(user, model.CurrentPassword);
            if (!checkPasswordResult)
            {
                _logger.LogWarning($"{user.Id}修改密碼，目前密碼錯誤");
                return BadRequest();
            }
            
            var changePasswordResult = await _userManager.ChangePasswordAsync(user, model.CurrentPassword, model.NewPassword);
            if (changePasswordResult.Succeeded)
            {
                _logger.LogInformation($"{user.Id}修改密碼成功");
                return Ok();
            }
            
            _logger.LogError($"{user.Id}修改密碼失敗");
            return BadRequest();
        }

        [Authorize]
        [HttpGet("{userId}/profile", Name = nameof(GetProfile))]
        public async Task<ActionResult<UserProfileViewModel>> GetProfile(string userId)
        {
            var user = await _userManager.FindByIdAsync(userId);
            if (user == null)
            {
                return NotFound();
            }

            var model = _mapper.Map<UserProfileViewModel>(user);
            
            return Ok(model);
        }
        
        [Authorize]
        [HttpPost("{userId}/profile", Name = nameof(ChangeProfile))]
        public async Task<IActionResult> ChangeProfile(string userId, UserProfileUpdateViewModel model)
        {
            var user = await _userManager.FindByIdAsync(userId);
            if (user == null)
            {
                return NotFound();
            }

            user.Name = model.Name;

            var result = await _userManager.UpdateAsync(user);
            if (result.Succeeded)
            {
                return Ok();
            }

            return BadRequest();
        }
    }
}