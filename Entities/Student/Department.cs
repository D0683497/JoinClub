using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace JoinClub.Entities.Student
{
    public class Department
    {
        public Department()
        {
            DepartmentId = Guid.NewGuid().ToString();
        }
        
        [Key]
        public string DepartmentId { get; set; }
        
        public string DepartmentName { get; set; }
        
        public string CollegeId { get; set; }
        public College College { get; set; }

        public ICollection<Class> Classes { get; set; }
    }
}