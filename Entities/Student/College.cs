using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace JoinClub.Entities.Student
{
    public class College
    {
        public College()
        {
            CollegeId = Guid.NewGuid().ToString();
        }
        
        [Key]
        public string CollegeId { get; set; }
        
        public string CollegeName { get; set; }

        public string DegreeId { get; set; }
        public Degree Degree { get; set; }

        public ICollection<Department> Departments { get; set; }
    }
}