using JoinClub.Data.EntityConfigurations;
using JoinClub.Entities.Identity;
using Microsoft.AspNetCore.Identity.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore;

namespace JoinClub.Data
{
    public class JoinClubDbContext : IdentityDbContext<ApplicationUser, ApplicationRole, string, ApplicationUserClaim, ApplicationUserRole, ApplicationUserLogin, ApplicationRoleClaim, ApplicationUserToken>
    {
        public JoinClubDbContext(DbContextOptions<JoinClubDbContext> options) : base(options)
        {
            
        }

        #region Identity

        public override DbSet<ApplicationUser> Users { get; set; }
        public override DbSet<ApplicationUserClaim> UserClaims { get; set; }
        public override DbSet<ApplicationUserLogin> UserLogins { get; set; }
        public override DbSet<ApplicationUserToken> UserTokens { get; set; }
        public override DbSet<ApplicationUserRole> UserRoles { get; set; }
        public override DbSet<ApplicationRole> Roles { get; set; }
        public override DbSet<ApplicationRoleClaim> RoleClaims { get; set; }

        #endregion

        protected override void OnModelCreating(ModelBuilder builder)
        {
            base.OnModelCreating(builder);
            
            IdentityConfigurations.IdentityRelation(builder);
        }
    }
}