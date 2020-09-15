using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Claims;
using System.Threading.Tasks;
using AutoMapper;
using JoinClub.Data;
using JoinClub.Entities.Application;
using JoinClub.Helpers;
using JoinClub.Models.User;
using JoinClub.Repositories.Interfaces;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace JoinClub.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class UsersController : ControllerBase
    {
        private readonly ILogger<UsersController> _logger;
        private readonly IUserRepository _userRepository;
        private readonly IMapper _mapper;
        private readonly UserManager<ApplicationUser> _userManager;
        private readonly ApplicationDbContext _applicationDbContext;

        public UsersController(ILogger<UsersController> logger, IUserRepository userRepository, IMapper mapper, UserManager<ApplicationUser> userManager, ApplicationDbContext applicationDbContext)
        {
            _logger = logger;
            _userRepository = userRepository;
            _mapper = mapper;
            _userManager = userManager;
            _applicationDbContext = applicationDbContext;
        }

        [HttpGet(Name = nameof(GetAllUsers))]
        public async Task<ActionResult<IEnumerable<UserViewModel>>> GetAllUsers([FromQuery] UserResourceParameters parameters)
        {
            var skipNumber = parameters.PageSize * (parameters.PageNumber - 1);
            var takeNumber = parameters.PageSize;

            var entities = await _userRepository.GetAllUsersAsync(skipNumber, takeNumber);

            var models = _mapper.Map<IEnumerable<UserViewModel>>(entities);

            return Ok(models);
        }
        
        [HttpGet("length", Name = nameof(GetAllUsersLength))]
        public async Task<ActionResult<int>> GetAllUsersLength()
        {
            return Ok(await _userRepository.GetAllUsersLengthAsync());
        }

        [HttpPost("{userId}", Name = nameof(UpdateUser))]
        public async Task<IActionResult> UpdateUser(string userId, UserUpdateViewModel model)
        {
            var user = await _userManager.FindByIdAsync(userId);
            if (user == null)
            {
                return NotFound();
            }

            var claim = await _userManager.GetClaimsAsync(user);

            if (user.Email != model.Email)
            {
                if (!await _userRepository.CanUpdateUserEmailAsync(userId, model.Email))
                {
                    ModelState.AddModelError("Email", $"{model.Email}已經被使用");
                    var problemDetails = new ValidationProblemDetails(ModelState)
                    {
                        Status = StatusCodes.Status400BadRequest,
                    };
                    return BadRequest(problemDetails);
                }

                user.Email = model.Email;
            }

            if (user.UserName != model.UserName)
            {
                if (!await _userRepository.CanUpdateUserUserNameAsync(userId, model.UserName))
                {
                    ModelState.AddModelError("UserName", $"{model.UserName}已經被使用");
                    var problemDetails = new ValidationProblemDetails(ModelState)
                    {
                        Status = StatusCodes.Status400BadRequest,
                    };
                    return BadRequest(problemDetails);
                }

                user.UserName = model.UserName;
                var userNameClaim = claim.FirstOrDefault(x => x.Type == ClaimTypes.Name);
                if (userNameClaim == null) { return BadRequest(); }

                if (await _userManager.RemoveClaimAsync(user, userNameClaim) != IdentityResult.Success)
                {
                    return BadRequest();
                }
                if (await _userManager.AddClaimAsync(user, new Claim(ClaimTypes.Name, model.UserName)) != IdentityResult.Success)
                {
                    return BadRequest();
                }
            }

            if (user.PhoneNumber != model.PhoneNumber)
            {
                if (!await _userRepository.CanUpdateUserPhoneNumberAsync(userId, model.PhoneNumber))
                {
                    ModelState.AddModelError("PhoneNumber", $"{model.PhoneNumber}已經被使用");
                    var problemDetails = new ValidationProblemDetails(ModelState)
                    {
                        Status = StatusCodes.Status400BadRequest,
                    };
                    return BadRequest(problemDetails);
                }

                user.PhoneNumber = model.PhoneNumber;
            }

            if (user.NID != model.NID)
            {
                if (!await _userRepository.CanUpdateUserNIDAsync(userId, model.NID))
                {
                    ModelState.AddModelError("NID", $"{model.NID}已經被使用");
                    var problemDetails = new ValidationProblemDetails(ModelState)
                    {
                        Status = StatusCodes.Status400BadRequest,
                    };
                    return BadRequest(problemDetails);
                }

                user.NID = model.NID;
            }

            user.Name = model.Name;
            user.College = model.College;
            user.Department = model.Department;
            user.Class = model.Class;

            var result = await _userManager.UpdateAsync(user);
            if (result.Succeeded)
            {
                return Ok();
            }

            return BadRequest();
        }
    }
}