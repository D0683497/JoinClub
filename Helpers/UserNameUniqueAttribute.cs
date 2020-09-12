using System.ComponentModel.DataAnnotations;
using JoinClub.Entities.Application;
using Microsoft.AspNetCore.Identity;

namespace JoinClub.Helpers
{
    public class UserNameUniqueAttribute : ValidationAttribute
    {
        protected override ValidationResult IsValid(object value, ValidationContext validationContext)
        {
            var userManager = (UserManager<ApplicationUser>)validationContext.GetService(typeof(UserManager<ApplicationUser>));
            var result = userManager.FindByNameAsync(value.ToString()).Result;

            if (result != null)
            {
                return new ValidationResult(GetErrorMessage(value.ToString()));
            }
            
            return ValidationResult.Success;
        }
        
        private string GetErrorMessage(string userName)
        {
            return $"{userName} 已經被使用";
        }
    }
}