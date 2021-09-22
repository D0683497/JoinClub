using JoinClub.Entities.Identity;
using Microsoft.EntityFrameworkCore;

namespace JoinClub.Data.EntityConfigurations
{
    public static class IdentityConfigurations
    {
        public static void IdentityRelation(ModelBuilder builder)
        {
            builder.Entity<ApplicationUser>(b =>
            {
                b.HasMany(e => e.Claims)
                    .WithOne(uc => uc.User)
                    .HasForeignKey(uc => uc.UserId);
                b.HasMany(e => e.Logins)
                    .WithOne(ul => ul.User)
                    .HasForeignKey(ul => ul.UserId);
                b.HasMany(e => e.Tokens)
                    .WithOne(ut => ut.User)
                    .HasForeignKey(ut => ut.UserId);
                b.HasMany(e => e.UserRoles)
                    .WithOne(ur => ur.User)
                    .HasForeignKey(ur => ur.UserId);
            });
            
            builder.Entity<ApplicationRole>(b =>
            {
                b.HasMany(e => e.UserRoles)
                    .WithOne(e => e.Role)
                    .HasForeignKey(ur => ur.RoleId);
                b.HasMany(e => e.RoleClaims)
                    .WithOne(e => e.Role)
                    .HasForeignKey(rc => rc.RoleId);
            });
            
            builder.Entity<ApplicationUserClaim>();
            
            builder.Entity<ApplicationUserLogin>(b =>
            {
                b.HasKey(l => new { l.LoginProvider, l.ProviderKey });
            });
            
            builder.Entity<ApplicationUserToken>(b => 
            {
                b.HasKey(t => new { t.UserId, t.LoginProvider, t.Name });
            });

            builder.Entity<ApplicationUserRole>(b =>
            {
                b.HasKey(r => new { r.UserId, r.RoleId });
            });
            
            builder.Entity<ApplicationRole>();
            
            builder.Entity<ApplicationRoleClaim>();
        }
    }
}