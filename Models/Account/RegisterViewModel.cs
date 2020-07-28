using System.ComponentModel.DataAnnotations;

namespace JoinClub.Models.Account
{
    public class RegisterViewModel
    {
        [Required(ErrorMessage = "{0} 是必填的")]
        [EmailAddress(ErrorMessage = "{0} 格式錯誤")]
        [Display(Name = "電子郵件")]
        public string Email { get; set; }

        [Required(ErrorMessage = "{0} 是必填的")]
        [Display(Name = "使用者名稱")]
        public string UserName { get; set; }

        [Required(ErrorMessage = "{0} 是必填的")]
        [StringLength(100, ErrorMessage = "The {0} must be at least {2} characters long.", MinimumLength = 4)]
        [DataType(DataType.Password)]
        [Display(Name = "密碼")]
        public string Password { get; set; }

        [Required(ErrorMessage = "{0} 是必填的")]
        [Compare("確認密碼", ErrorMessage = "Password and Confirm Password must match")]
        public string ConfirmPassword { get; set; }
    }
}