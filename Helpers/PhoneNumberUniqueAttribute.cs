using System.ComponentModel.DataAnnotations;
using JoinClub.Entities.Application;
using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;

namespace JoinClub.Helpers
{
    public class PhoneNumberUniqueAttribute : ValidationAttribute
    {
        protected override ValidationResult IsValid(object value, ValidationContext validationContext)
        {
            if (value == null)
            {
                return ValidationResult.Success;
            }
            
            var userManager = (UserManager<ApplicationUser>)validationContext.GetService(typeof(UserManager<ApplicationUser>));
            var result = userManager.Users.FirstOrDefaultAsync(x => x.PhoneNumber == value.ToString()).Result;

            if (result != null)
            {
                return new ValidationResult(GetErrorMessage(value.ToString()));
            }
            
            return ValidationResult.Success;
        }
        
        private string GetErrorMessage(string phoneNumber)
        {
            return $"{phoneNumber} 已經被使用";
        }
    }
}