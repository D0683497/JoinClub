using Microsoft.AspNetCore.Identity;

namespace JoinClub.Entities.Application
{
    public class ApplicationUser : IdentityUser
    {
        /// <summary>
        /// 學號
        /// </summary>
        public string NID { get; set; }
        
        /// <summary>
        /// 真實姓名
        /// </summary>
        public string Name { get; set; }

        /// <summary>
        /// 學院
        /// </summary>
        public string College { get; set; }

        /// <summary>
        /// 系所
        /// </summary>
        public string Department { get; set; }

        /// <summary>
        /// 班級
        /// </summary>
        public string Class { get; set; }
    }
}