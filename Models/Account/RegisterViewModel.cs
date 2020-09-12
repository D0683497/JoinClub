using System.ComponentModel.DataAnnotations;
using JoinClub.Helpers;

namespace JoinClub.Models.Account
{
    public class RegisterViewModel
    {
        [Required(ErrorMessage = "{0}是必填的")]
        [EmailAddress(ErrorMessage = "{0}格式錯誤")]
        [EmailUnique]
        [Display(Name = "電子郵件")]
        public string Email { get; set; }

        [Required(ErrorMessage = "{0}是必填的")]
        [RegularExpression(@"^.[\w\-\.\@\+\#\$\%\\\/\(\)\[\]\*\&\:\>\<\^\!\{\}\=]+$",
            ErrorMessage = "{0}只能是字母或數字或 - . _ @ + # $ % \\ / ( ) [ ] * & : > < ^ ! {{ }} =")]
        [UserNameUnique]
        [Display(Name = "使用者名稱")]
        public string UserName { get; set; }

        [Required(ErrorMessage = "{0}是必填的")]
        [StringLength(64, ErrorMessage = "{0}長度需介於{2}到{1}之間", MinimumLength = 8)]
        [Display(Name = "密碼")]
        public string Password { get; set; }
        
        [Required(ErrorMessage = "{0}是必填的")]
        [StringLength(64, ErrorMessage = "{0}長度需介於{2}到{1}之間", MinimumLength = 8)]
        [Compare("Password", ErrorMessage = "確認密碼與密碼不相同")]
        [Display(Name = "確認密碼")]
        public string PasswordConfirm { get; set; }
        
        [Phone(ErrorMessage = "{0}格式錯誤")]
        [Display(Name = "手機號碼")]
        public string PhoneNumber { get; set; }
        
        [Required(ErrorMessage = "{0}是必填的")]
        [NIDUnique]
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