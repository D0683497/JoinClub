using FluentValidation;

namespace JoinClub.Utilities
{
    public static class RuleBuilderExtensions
    {
        public static IRuleBuilderOptions<T, string> Password<T>(this IRuleBuilder<T, string> ruleBuilder)     
        {
            // (?=.*[a-z])  // RequireLowercase
            // (?=.*[A-Z])  // RequireUppercase
            // (?=.*\d) // RequireDigit
            // (?=.*\W]) // RequireNonAlphanumeric
            
            return ruleBuilder
                .Matches(@"(?=.*\d)")
                .WithName("密碼")
                .WithMessage("{PropertyName}至少需要一位數字")
                .OverridePropertyName("password")
                .Matches(@"(?=.*[a-z])")
                .WithName("密碼")
                .WithMessage("{PropertyName}至少需要一位小寫字母")
                .OverridePropertyName("password");     
        }
    }
}