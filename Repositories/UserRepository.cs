using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using JoinClub.Data;
using JoinClub.Entities.Application;
using JoinClub.Repositories.Interfaces;
using Microsoft.EntityFrameworkCore;

namespace JoinClub.Repositories
{
    public class UserRepository : IUserRepository
    {
        private readonly ApplicationDbContext _applicationDbContext;

        public UserRepository(ApplicationDbContext applicationDbContext)
        {
            _applicationDbContext = applicationDbContext;
        }
        
        public async Task<IEnumerable<ApplicationUser>> GetAllUsersAsync(int skipNumber, int takeNumber)
        {
            return await _applicationDbContext.Users
                .Skip(skipNumber)
                .Take(takeNumber)
                .ToListAsync();
        }
        
        public async Task<int> GetAllUsersLengthAsync()
        {
            return await _applicationDbContext.Users
                .CountAsync();
        }
    }
}