using System.ComponentModel.DataAnnotations;

namespace JoinClub.Models.Account
{
    public class ChangePasswordViewModel
    {
        [Required(ErrorMessage = "{0}是必填的")]
        [Display(Name = "使用者識別碼")]
        public string UserId { get; set; }

        [Required(ErrorMessage = "{0}是必填的")]
        [StringLength(64, ErrorMessage = "{0}長度需介於{2}到{1}之間", MinimumLength = 8)]
        [Display(Name = "舊密碼")]
        public string OldPassword { get; set; }
        
        [Required(ErrorMessage = "{0}是必填的")]
        [StringLength(64, ErrorMessage = "{0}長度需介於{2}到{1}之間", MinimumLength = 8)]
        [Display(Name = "新密碼")]
        public string NewPassword { get; set; }
    }
}