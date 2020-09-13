using System.ComponentModel.DataAnnotations;

namespace JoinClub.Models.User
{
    public class UserViewModel
    {
        [Display(Name = "識別碼")]
        public string Id { get; set; }
        
        [Display(Name = "電子郵件")]
        public string Email { get; set; }

        [Display(Name = "使用者名稱")]
        public string UserName { get; set; }

        [Display(Name = "手機號碼")]
        public string PhoneNumber { get; set; }
        
        [Display(Name = "學號")]
        public string NID { get; set; }
        
        [Display(Name = "真實姓名")]
        public string Name { get; set; }

        [Display(Name = "學院")]
        public string College { get; set; }

        [Display(Name = "系所")]
        public string Department { get; set; }

        [Display(Name = "班級")]
        public string Class { get; set; }
    }
}