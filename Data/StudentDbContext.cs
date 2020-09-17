using JoinClub.Entities.Student;
using Microsoft.EntityFrameworkCore;

namespace JoinClub.Data
{
    public class StudentDbContext : DbContext
    {
        public StudentDbContext(DbContextOptions<StudentDbContext> options) : base(options)
        {
            
        }

        public DbSet<Degree> Degrees { get; set; }
        public DbSet<College> Colleges { get; set; }
        public DbSet<Department> Departments { get; set; }
        public DbSet<Class> Classes { get; set; }

        protected override void OnModelCreating(ModelBuilder builder)
        {
            base.OnModelCreating(builder);
            
            // Degree 跟 College 一對多
            builder.Entity<College>()
                .HasOne(college => college.Degree)
                .WithMany(degree => degree.Colleges)
                .HasForeignKey(college => college.DegreeId);

            // College 跟 Department 一對多
            builder.Entity<Department>()
                .HasOne(department => department.College)
                .WithMany(college => college.Departments)
                .HasForeignKey(department => department.CollegeId);

            // Department 跟 Class 一對多
            builder.Entity<Class>()
                .HasOne(@class => @class.Department)
                .WithMany(department => department.Classes)
                .HasForeignKey(department => department.DepartmentId);
            
            
        }
    }
}