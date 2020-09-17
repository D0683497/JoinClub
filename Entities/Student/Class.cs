using System;
using System.ComponentModel.DataAnnotations;

namespace JoinClub.Entities.Student
{
    public class Class
    {
        public Class()
        {
            ClassId = Guid.NewGuid().ToString();
        }
        
        [Key]
        public string ClassId { get; set; }
        
        public string ClassName { get; set; }
        
        public string DepartmentId { get; set; }
        public Department Department { get; set; }
    }
}