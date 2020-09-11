using System.ComponentModel.DataAnnotations;

namespace JoinClub.Models.Account
{
    public class LoginViewModel
    {
        [Required(ErrorMessage = "{0}是必填的")]
        [RegularExpression(@"^.[\w\-\.\@\+\#\$\%\\\/\(\)\[\]\*\&\:\>\<\^\!\{\}\=]+$",
            ErrorMessage = "{0}只能是字母或數字或 - . _ @ + # $ % \\ / ( ) [ ] * & : > < ^ ! {{ }} =")] // \w 等於[A-Za-z0-9_]
        [Display(Name = "使用者名稱")]
        public string UserName { get; set; }

        [Required(ErrorMessage = "{0}是必填的")]
        [StringLength(64, ErrorMessage = "{0}長度需介於{2}到{1}之間", MinimumLength = 8)]
        [Display(Name = "密碼")]
        public string Password { get; set; }
    }
}