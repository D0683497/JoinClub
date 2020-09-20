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
        private readonly ApplicationDbContext _applicationDbContext;

        public UsersController(
            ILogger<UsersController> logger, 
            IUserRepository userRepository, 
            IMapper mapper, 
            ApplicationDbContext applicationDbContext)
        {
            _logger = logger;
            _userRepository = userRepository;
            _mapper = mapper;
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
            var user = await _userRepository.GetUserByIdAsync(userId);
            if (user == null)
            {
                return NotFound();
            }

            using (var transaction = _applicationDbContext.Database.BeginTransaction())
            {
                if (!await _userRepository.UpdateEmailByUserAsync(user, model.Email))
                {
                    ModelState.AddModelError("Email", $"{model.Email}已經被使用");
                    var problemDetails = new ValidationProblemDetails(ModelState)
                    {
                        Status = StatusCodes.Status400BadRequest,
                    };
                    await transaction.RollbackAsync();
                    return BadRequest(problemDetails);
                }

                if (!await _userRepository.UpdateNameByUserAsync(user, model.UserName))
                {
                    ModelState.AddModelError("UserName", $"{model.UserName}已經被使用");
                    var problemDetails = new ValidationProblemDetails(ModelState)
                    {
                        Status = StatusCodes.Status400BadRequest,
                    };
                    await transaction.RollbackAsync();
                    return BadRequest(problemDetails);   
                }

                if (!await _userRepository.UpdatePhoneNumberByUserAsync(user, model.PhoneNumber))
                {
                    ModelState.AddModelError("PhoneNumber", $"{model.PhoneNumber}已經被使用");
                    var problemDetails = new ValidationProblemDetails(ModelState)
                    {
                        Status = StatusCodes.Status400BadRequest,
                    };
                    await transaction.RollbackAsync();
                    return BadRequest(problemDetails);
                }

                if (!await _userRepository.UpdateNIDByUserAsync(user, model.NID))
                {
                    ModelState.AddModelError("NID", $"{model.NID}已經被使用");
                    var problemDetails = new ValidationProblemDetails(ModelState)
                    {
                        Status = StatusCodes.Status400BadRequest,
                    };
                    await transaction.RollbackAsync();
                    return BadRequest(problemDetails);
                }

                if (!await _userRepository.UpdateNameByUserAsync(user, model.Name))
                {
                    await transaction.RollbackAsync();
                    return BadRequest();
                }

                if (!await _userRepository.UpdateCollegeByUserAsync(user, model.College))
                {
                    await transaction.RollbackAsync();
                    return BadRequest();
                }

                if (!await _userRepository.UpdateDepartmentByUserAsync(user, model.Department))
                {
                    await transaction.RollbackAsync();
                    return BadRequest();
                }

                if (!await _userRepository.UpdateClassByUserAsync(user, model.Class))
                {
                    await transaction.RollbackAsync();
                    return BadRequest();
                }

                await transaction.CommitAsync();
            }

            return Ok();
        }

        [HttpDelete("{userId}", Name = nameof(DeleteUser))]
        public async Task<IActionResult> DeleteUser(string userId)
        {
            var user = await _userRepository.GetUserByIdAsync(userId);
            if (user == null)
            {
                return NotFound();
            }

            if (!await _userRepository.DeleteUserByUser(user))
            {
                return BadRequest();
            }

            return Ok();
        }

        [HttpGet("{userId}", Name = nameof(GetUserById))]
        public async Task<ActionResult<UserViewModel>> GetUserById(string userId)
        {
            var user = await _userRepository.GetUserByIdAsync(userId);
            if (user == null)
            {
                return NotFound();
            }

            var model = _mapper.Map<UserViewModel>(user);

            return Ok(model);
        }
    }
}