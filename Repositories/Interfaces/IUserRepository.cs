using System.Collections.Generic;
using System.Threading.Tasks;
using JoinClub.Entities.Application;

namespace JoinClub.Repositories.Interfaces
{
    public interface IUserRepository
    {
        Task<IEnumerable<ApplicationUser>> GetAllUsersAsync(int skipNumber, int takeNumber);

        Task<int> GetAllUsersLengthAsync();

        Task<bool> CanUpdateUserEmailAsync(string userId, string updateEmail);

        Task<bool> CanUpdateUserUserNameAsync(string userId, string updateUserName);

        Task<bool> CanUpdateUserPhoneNumberAsync(string userId, string updatePhoneNumber);

        Task<bool> CanUpdateUserNIDAsync(string userId, string updateNID);
    }
}