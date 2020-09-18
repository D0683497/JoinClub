using System.ComponentModel.DataAnnotations;

namespace JoinClub.Models.User
{
    public class UserProfileUpdateViewModel
    {
        [Required(ErrorMessage = "{0}是必填的")]
        [Display(Name = "真實姓名")]
        public string Name { get; set; }
    }
}