using System.Collections.Generic;
using System.Security.Claims;
using System.Threading.Tasks;
using JoinClub.Entities.Application;

namespace JoinClub.Repositories.Interfaces
{
    public interface IUserRepository
    {
        Task<IEnumerable<ApplicationUser>> GetAllUsersAsync(int skipNumber, int takeNumber);

        Task<int> GetAllUsersLengthAsync();

        Task<ApplicationUser> GetUserByIdAsync(string userId);

        Task<bool> UpdateEmailByUserAsync(ApplicationUser user, string email);

        Task<bool> UpdateUserNameByUserAsync(ApplicationUser user, string userName);

        Task<bool> UpdatePhoneNumberByUserAsync(ApplicationUser user, string phoneNumber);

        Task<bool> UpdateNIDByUserAsync(ApplicationUser user, string nid);

        Task<bool> UpdateNameByUserAsync(ApplicationUser user, string name);
        
        Task<bool> UpdateCollegeByUserAsync(ApplicationUser user, string college);
        
        Task<bool> UpdateDepartmentByUserAsync(ApplicationUser user, string department);
        
        Task<bool> UpdateClassByUserAsync(ApplicationUser user, string @class);

        Task<bool> DeleteUserByUser(ApplicationUser user);
    }
}