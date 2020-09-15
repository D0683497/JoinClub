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

        public AccountController(
            ILogger<AccountController> logger, 
            UserManager<ApplicationUser> userManager, 
            IMapper mapper)
        {
            _logger = logger;
            _userManager = userManager;
            _mapper = mapper;
        }

        [AllowAnonymous]
        [HttpPost("register", Name = nameof(Register))]
        public async Task<IActionResult> Register(RegisterViewModel model)
        {
            var entity = _mapper.Map<ApplicationUser>(model);
            
            var createUserResult = await _userManager.CreateAsync(entity, model.Password);
            if (createUserResult.Succeeded)
            {
                _logger.LogInformation($"註冊{model.UserName}成功");
                return Ok();
            }
            
            return BadRequest("註冊失敗");
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