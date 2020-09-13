using System.Collections.Generic;
using System.Threading.Tasks;
using JoinClub.Entities.Application;

namespace JoinClub.Repositories.Interfaces
{
    public interface IUserRepository
    {
        Task<IEnumerable<ApplicationUser>> GetAllUsersAsync(int skipNumber, int takeNumber);

        Task<int> GetAllUsersLengthAsync();
    }
}