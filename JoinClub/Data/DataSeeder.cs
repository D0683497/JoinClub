using System;
using System.Security.Claims;
using System.Threading.Tasks;
using JoinClub.Entities.Identity;
using Microsoft.AspNetCore.Identity;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;

namespace JoinClub.Data
{
    public class DataSeeder
    {
        public static async Task Initialize(IHost host)
        {
            using (var scope = host.Services.CreateScope())
            {
                var services = scope.ServiceProvider;
                var logger = services.GetRequiredService<ILogger<DataSeeder>>();
                var dbContext = services.GetRequiredService<JoinClubDbContext>();
                var configuration = services.GetRequiredService<IConfiguration>();

                logger.LogInformation("開始創建資料庫");
                if (await dbContext.Database.EnsureCreatedAsync())
                {
                    logger.LogInformation("開始創建角色及角色聲明");
                    await CreateRoleAsync(services, configuration);
                    logger.LogInformation("創建角色及角色聲明完成");

                    logger.LogInformation("開始創建使用者");
                    await CreateUserAsync(services, configuration);
                    logger.LogInformation("創建使用者完成");
                }
                else
                {
                    logger.LogInformation("資料庫已存在");
                }
            }
        }

        private static async Task CreateRoleAsync(IServiceProvider services, IConfiguration configuration)
        {
            var roleManager = services.GetRequiredService<RoleManager<ApplicationRole>>();

            var role = new ApplicationRole { Name = $"{configuration["User:RoleName"]}" };

            var claim = new Claim(ClaimTypes.Role, $"{configuration["User:RoleName"]}");

            await roleManager.CreateAsync(role);

            await roleManager.AddClaimAsync(role, claim);
        }

        private static async Task CreateUserAsync(IServiceProvider services, IConfiguration configuration)
        {
            var userManager = services.GetRequiredService<UserManager<ApplicationUser>>();

            var user = new ApplicationUser
            {
                UserName = $"{configuration["User:UserName"]}",
                Email = $"{configuration["User:Email"]}",
                EmailConfirmed = true,
                Enable = true,
                LockoutEnabled = false
            };

            await userManager.CreateAsync(user, $"{configuration["User:Password"]}");

            await userManager.AddToRoleAsync(user, $"{configuration["User:RoleName"]}");
        }
    }
}