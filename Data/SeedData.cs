using System;
using System.Collections.Generic;
using System.Security.Claims;
using JoinClub.Entities.Application;
using Microsoft.AspNetCore.Identity;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;

namespace JoinClub.Data
{
    public class SeedData
    {
        public static void EnsureSeedData(IHost host)
        {
            using (var scope = host.Services.CreateScope())
            {
                var services = scope.ServiceProvider;
                var logger = services.GetRequiredService<ILogger<SeedData>>();
                
                #region Database

                logger.LogInformation("開始創建資料庫");
                var dbContext = services.GetRequiredService<ApplicationDbContext>();
                dbContext.Database.EnsureCreated();
                logger.LogInformation("創資料庫完成");

                #endregion
                
                #region Role

                logger.LogInformation("開始創建角色及角色聲明");
                CreateRole(services, logger);
                logger.LogInformation("創建角色及角色聲明完成");

                #endregion
                
                #region User

                logger.LogInformation("開始創建使用者");
                CreateUser(services, logger);
                logger.LogInformation("創建使用者完成");

                #endregion
            }
        }
        
        private static void CreateRole(IServiceProvider services, ILogger<SeedData> logger)
        {
            try
            {
                var roleManager = services.GetRequiredService<RoleManager<ApplicationRole>>();

                #region Admin

                var result = roleManager.CreateAsync(new ApplicationRole { Name = "Admin" }).Result;
                if (result.Succeeded)
                {
                    logger.LogInformation("建立Admin角色成功");

                    var admin = roleManager.FindByNameAsync("Admin").Result;
                    var adminClaim = new Claim(ClaimTypes.Role, "Admin");

                    result = roleManager.AddClaimAsync(admin, adminClaim).Result;
                    if (result.Succeeded)
                    {
                        logger.LogInformation("建立Admin角色聲明成功");
                    }
                    else
                    {
                        logger.LogError("建立Admin角色聲明失敗");
                    }
                }
                else
                {
                    logger.LogError("建立Admin角色失敗");
                }

                #endregion
                
                #region Staff

                result = roleManager.CreateAsync(new ApplicationRole { Name = "Staff" }).Result;
                if (result.Succeeded)
                {
                    logger.LogInformation("建立Staff角色成功");

                    var staff = roleManager.FindByNameAsync("Staff").Result;
                    var staffClaim = new Claim(ClaimTypes.Role, "Staff");

                    result = roleManager.AddClaimAsync(staff, staffClaim).Result;
                    if (result.Succeeded)
                    {
                        logger.LogInformation("建立Staff角色聲明成功");
                    }
                    else
                    {
                        logger.LogError("建立Staff角色聲明失敗");
                    }
                }
                else
                {
                    logger.LogError("建立Staff角色失敗");
                }

                #endregion

                #region Member

                result = roleManager.CreateAsync(new ApplicationRole { Name = "Member" }).Result;
                if (result.Succeeded)
                {
                    logger.LogInformation("建立Member角色成功");

                    var member = roleManager.FindByNameAsync("Member").Result;
                    var memberClaim = new Claim(ClaimTypes.Role, "Member");

                    result = roleManager.AddClaimAsync(member, memberClaim).Result;
                    if (result.Succeeded)
                    {
                        logger.LogInformation("建立Member角色聲明成功");
                    }
                    else
                    {
                        logger.LogError("建立Member角色聲明失敗");
                    }
                }
                else
                {
                    logger.LogError("建立Member角色失敗");
                }

                #endregion
            }
            catch (Exception e)
            {
                logger.LogError($"發生未知錯誤\n{e.ToString()}");
                throw;
            }
        }

        private static void CreateUser(IServiceProvider services, ILogger<SeedData> logger)
        {
            try
            {
                var userManager = services.GetRequiredService<UserManager<ApplicationUser>>();
                var configuration = services.GetRequiredService<IConfiguration>();
                
                #region Admin
                
                var admin = new ApplicationUser
                {
                    Email = configuration["UserSettings:Admin:Email"],
                    EmailConfirmed = true,
                    UserName = configuration["UserSettings:Admin:UserName"],
                    PhoneNumber = configuration["UserSettings:Admin:UserName"],
                    PhoneNumberConfirmed = true,
                    NID = configuration["UserSettings:Admin:NID"],
                    Name = configuration["UserSettings:Admin:Name"],
                    College = configuration["UserSettings:Admin:College"],
                    Department = configuration["UserSettings:Admin:Department"],
                    Class = configuration["UserSettings:Admin:Class"],
                    LockoutEnabled = false
                };

                var result = userManager.CreateAsync(admin, configuration["UserSettings:Admin:Password"]).Result;
                if (result.Succeeded)
                {
                    logger.LogInformation("建立Admin使用者成功");
                }
                else
                {
                    logger.LogError("建立Admin使用者失敗");
                }

                var currentUser = userManager.FindByNameAsync(configuration["UserSettings:Admin:UserName"]).Result;
                result = userManager.AddToRoleAsync(currentUser, "Admin").Result;
                if (result.Succeeded)
                {
                    logger.LogInformation("Admin使用者添加角色成功");
                    var claims = new List<Claim>
                    {
                        new Claim(ClaimTypes.NameIdentifier, string.IsNullOrEmpty(currentUser.Id) ? "" : currentUser.Id),
                        new Claim(ClaimTypes.Name, string.IsNullOrEmpty(currentUser.UserName) ? "" : currentUser.UserName),
                    };
                    var addClaimResult = userManager.AddClaimsAsync(currentUser, claims).Result;
                    if (addClaimResult.Succeeded)
                    {
                        logger.LogInformation("Admin使用者添加聲明成功");
                    }
                    else
                    {
                        logger.LogError("Admin使用者添加聲明失敗");
                    }
                }
                else
                {
                    logger.LogError("Admin使用者添加角色失敗");
                }

                #endregion
            }
            catch (Exception e)
            {
                logger.LogError($"發生未知錯誤\n{e.ToString()}");
                throw;
            }
        }
    }
}