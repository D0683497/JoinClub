using System.ComponentModel.DataAnnotations;
using JoinClub.Entities.Application;
using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;

namespace JoinClub.Helpers
{
    public class NIDUniqueAttribute : ValidationAttribute
    {
        protected override ValidationResult IsValid(object value, ValidationContext validationContext)
        {
            var userManager = (UserManager<ApplicationUser>)validationContext.GetService(typeof(UserManager<ApplicationUser>));
            var result = userManager.Users.FirstOrDefaultAsync(x => x.NID == value.ToString()).Result;

            if (result != null)
            {
                return new ValidationResult(GetErrorMessage(value.ToString()));
            }
            
            return ValidationResult.Success;
        }
        
        private string GetErrorMessage(string NID)
        {    
            return $"{NID} 已經被使用";
        }
    }
}