using System;
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

        public async Task<bool> CanUpdateUserEmailAsync(string userId, string updateEmail)
        {
            var user = await _applicationDbContext.Users
                .Where(x => x.Email == updateEmail)
                .FirstOrDefaultAsync();
            
            if (user == null) { return true; }

            if (user.Id == userId) { return true; }

            return false;
        }
        
        public async Task<bool> CanUpdateUserUserNameAsync(string userId, string updateUserName)
        {
            var user = await _applicationDbContext.Users
                .Where(x => x.UserName == updateUserName)
                .FirstOrDefaultAsync();
            
            if (user == null) { return true; }

            if (user.Id == userId) { return true; }

            return false;
        }
        
        public async Task<bool> CanUpdateUserPhoneNumberAsync(string userId, string updatePhoneNumber)
        {
            if (updatePhoneNumber == String.Empty) { return true; }
            
            var user = await _applicationDbContext.Users
                .Where(x => x.PhoneNumber == updatePhoneNumber)
                .FirstOrDefaultAsync();
            
            if (user == null) { return true; }

            if (user.Id == userId) { return true; }

            return false;
        }
        
        public async Task<bool> CanUpdateUserNIDAsync(string userId, string updateNID)
        {
            var user = await _applicationDbContext.Users
                .Where(x => x.NID == updateNID)
                .FirstOrDefaultAsync();
            
            if (user == null) { return true; }

            if (user.Id == userId) { return true; }

            return false;
        }

        public void UpdateUser(ApplicationUser user)
        {
            _applicationDbContext.Entry(user).Property("Email").IsModified = true;
            _applicationDbContext.Entry(user).Property("UserName").IsModified = true;
            _applicationDbContext.Entry(user).Property("PhoneNumber").IsModified = true;
            _applicationDbContext.Entry(user).Property("NID").IsModified = true;
            _applicationDbContext.Entry(user).Property("Name").IsModified = true;
            _applicationDbContext.Entry(user).Property("College").IsModified = true;
            _applicationDbContext.Entry(user).Property("Department").IsModified = true;
            _applicationDbContext.Entry(user).Property("Class").IsModified = true;
        }
        
        public async Task<bool> SaveAsync()
        {
            return await _applicationDbContext.SaveChangesAsync() >= 0;
        }
    }
}