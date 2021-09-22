using System.ComponentModel.DataAnnotations;
using System.Text.Json.Serialization;

namespace JoinClub.Dtos.Account
{
    public class LoginResponseDto
    {
        [JsonPropertyName("token")]
        [Display(Name = "權杖")]
        public string Token { get; set; }
    }
}
