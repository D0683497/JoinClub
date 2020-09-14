using System.ComponentModel.DataAnnotations;

namespace JoinClub.Models.User
{
    public class UserUpdateViewModel
    {
        [Required(ErrorMessage = "{0}是必填的")]
        [EmailAddress(ErrorMessage = "{0}格式錯誤")]
        [Display(Name = "電子郵件")]
        public string Email { get; set; }

        [Required(ErrorMessage = "{0}是必填的")]
        [RegularExpression(@"^.[\w\-\.\@\+\#\$\%\\\/\(\)\[\]\*\&\:\>\<\^\!\{\}\=]+$",
            ErrorMessage = "{0}只能是字母或數字或 - . _ @ + # $ % \\ / ( ) [ ] * & : > < ^ ! {{ }} =")]
        [Display(Name = "使用者名稱")]
        public string UserName { get; set; }

        [Phone(ErrorMessage = "{0}格式錯誤")]
        [Display(Name = "手機號碼")]
        public string PhoneNumber { get; set; }
        
        [Required(ErrorMessage = "{0}是必填的")]
        [Display(Name = "學號")]
        public string NID { get; set; }
        
        [Required(ErrorMessage = "{0}是必填的")]
        [Display(Name = "真實姓名")]
        public string Name { get; set; }

        [Required(ErrorMessage = "{0}是必填的")]
        [Display(Name = "學院")]
        public string College { get; set; }

        [Required(ErrorMessage = "{0}是必填的")]
        [Display(Name = "系所")]
        public string Department { get; set; }

        [Required(ErrorMessage = "{0}是必填的")]
        [Display(Name = "班級")]
        public string Class { get; set; }
    }
}