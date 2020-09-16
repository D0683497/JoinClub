using System.ComponentModel.DataAnnotations;

namespace JoinClub.Models.Account
{
    public class ChangePasswordViewModel
    {
        [Required(ErrorMessage = "{0}是必填的")]
        [StringLength(64, ErrorMessage = "{0}長度需介於{2}到{1}之間", MinimumLength = 8)]
        [Display(Name = "目前密碼")]
        public string CurrentPassword { get; set; }
        
        [Required(ErrorMessage = "{0}是必填的")]
        [StringLength(64, ErrorMessage = "{0}長度需介於{2}到{1}之間", MinimumLength = 8)]
        [Display(Name = "新密碼")]
        public string NewPassword { get; set; }
        
        [Required(ErrorMessage = "{0}是必填的")]
        [StringLength(64, ErrorMessage = "{0}長度需介於{2}到{1}之間", MinimumLength = 8)]
        [Compare("NewPassword", ErrorMessage = "確認新密碼與新密碼不相同")]
        [Display(Name = "確認新密碼")]
        public string ConfirmNewPassword { get; set; }
    }
}