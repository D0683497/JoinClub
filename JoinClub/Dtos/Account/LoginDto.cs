using System.ComponentModel.DataAnnotations;
using System.Text.Json.Serialization;

namespace JoinClub.Dtos.Account
{
    public class LoginDto
    {
        [JsonPropertyName("username")]
        [Display(Name = "使用者名稱")]
        public string UserName { get; set; }

        [JsonPropertyName("password")]
        [Display(Name = "密碼")]
        public string Password { get; set; }
    }
}
