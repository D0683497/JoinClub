using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace JoinClub.Entities.Student
{
    public class Degree
    {
        public Degree()
        {
            DegreeId = Guid.NewGuid().ToString();
        }
        
        [Key]
        public string DegreeId { get; set; }
        
        public string DegreeName { get; set; }

        public ICollection<College> Colleges { get; set; }
    }
}