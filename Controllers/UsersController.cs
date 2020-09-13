using System.Collections.Generic;
using System.Threading.Tasks;
using AutoMapper;
using JoinClub.Helpers;
using JoinClub.Models.User;
using JoinClub.Repositories.Interfaces;
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

        public UsersController(ILogger<UsersController> logger, IUserRepository userRepository, IMapper mapper)
        {
            _logger = logger;
            _userRepository = userRepository;
            _mapper = mapper;
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
    }
}