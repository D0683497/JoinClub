using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Claims;
using System.Threading.Tasks;
using JoinClub.Data;
using JoinClub.Entities.Application;
using JoinClub.Repositories.Interfaces;
using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;

namespace JoinClub.Repositories
{
    public class UserRepository : IUserRepository
    {
        private readonly UserManager<ApplicationUser> _userManager;
        private readonly ApplicationDbContext _applicationDbContext;

        public UserRepository(UserManager<ApplicationUser> userManager, ApplicationDbContext applicationDbContext)
        {
            _userManager = userManager;
            _applicationDbContext = applicationDbContext;
        }

        public async Task<IEnumerable<ApplicationUser>> GetAllUsersAsync(int skipNumber, int takeNumber)
        {
            return await _userManager.Users
                .Skip(skipNumber)
                .Take(takeNumber)
                .ToListAsync();
        }
        
        public async Task<int> GetAllUsersLengthAsync()
        {
            return await _userManager.Users
                .CountAsync();
        }

        public async Task<ApplicationUser> GetUserByIdAsync(string userId)
        {
            return await _userManager.FindByIdAsync(userId);
        }

        public async Task<bool> UpdateEmailByUserAsync(ApplicationUser user, string email)
        {
            if (user.Email == email)
            {
                return true;
            }

            var canUpdate = !await _userManager.Users.AnyAsync(x => x.Email == email);
            if (canUpdate)
            {
                await _userManager.SetEmailAsync(user, email);
                return true;
            }

            return false;
        }

        public async Task<bool> UpdateUserNameByUserAsync(ApplicationUser user, string userName)
        {
            if (user.UserName == userName)
            {
                return true;
            }

            var canUpdate = !await _userManager.Users.AnyAsync(x => x.UserName == userName);
            if (canUpdate)
            {
                await _userManager.SetUserNameAsync(user, userName);
                
                var claims = await _userManager.GetClaimsAsync(user);
                var userNameClaim = claims.FirstOrDefault(x => x.Type == ClaimTypes.Name);
                await _userManager.RemoveClaimAsync(user, userNameClaim);
                await _userManager.AddClaimAsync(user, new Claim(ClaimTypes.Name, userName));
                
                return true;
            }

            return false;
        }

        public async Task<bool> UpdatePhoneNumberByUserAsync(ApplicationUser user, string phoneNumber)
        {
            if (user.PhoneNumber == phoneNumber)
            {
                return true;
            }
            
            if (String.IsNullOrEmpty(phoneNumber))
            {
                await _userManager.SetPhoneNumberAsync(user, phoneNumber);
                return true;
            }

            var canUpdate = !await _userManager.Users.AnyAsync(x => x.PhoneNumber == phoneNumber);
            if (canUpdate)
            {
                await _userManager.SetPhoneNumberAsync(user, phoneNumber);
                return true;
            }

            return false;
        }
        
        public async Task<bool> UpdateNIDByUserAsync(ApplicationUser user, string nid)
        {
            if (user.NID == nid)
            {
                return true;
            }

            var canUpdate = !await _userManager.Users.AnyAsync(x => x.NID == nid);
            if (canUpdate)
            {
                user.NID = nid;
                await _userManager.UpdateAsync(user);
                return true;
            }

            return false;
        }

        public async Task<bool> UpdateNameByUserAsync(ApplicationUser user, string name)
        {
            if (user.Name == name)
            {
                return true;
            }

            user.Name = name;
            await _userManager.UpdateAsync(user);
            return true;
        }
        
        public async Task<bool> UpdateCollegeByUserAsync(ApplicationUser user, string college)
        {
            if (user.College == college)
            {
                return true;
            }

            user.College = college;
            await _userManager.UpdateAsync(user);
            return true;
        }
        
        public async Task<bool> UpdateDepartmentByUserAsync(ApplicationUser user, string department)
        {
            if (user.Department == department)
            {
                return true;
            }

            user.Department = department;
            await _userManager.UpdateAsync(user);
            return true;
        }
        
        public async Task<bool> UpdateClassByUserAsync(ApplicationUser user, string @class)
        {
            if (user.Class == @class)
            {
                return true;
            }

            user.Class = @class;
            await _userManager.UpdateAsync(user);
            return true;
        }

        public async Task<bool> DeleteUserByUser(ApplicationUser user)
        {
            var claims = await _userManager.GetClaimsAsync(user);
            var roles = await _userManager.GetRolesAsync(user);
            
            if (roles.Any(x => x.Contains("Admin")))
            {
                return false;
            }
            
            using (var transaction = _applicationDbContext.Database.BeginTransaction())
            {
                if (await _userManager.RemoveClaimsAsync(user, claims) != IdentityResult.Success)
                {
                    await transaction.RollbackAsync();
                    return false;
                }

                if (await _userManager.RemoveFromRolesAsync(user, roles) != IdentityResult.Success)
                {
                    await transaction.RollbackAsync();
                    return false;
                }

                if (await _userManager.DeleteAsync(user) != IdentityResult.Success)
                {
                    await transaction.RollbackAsync();
                    return false;
                }

                await transaction.CommitAsync();
            }

            return true;
        }
    }
}