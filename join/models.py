from django.db import models
from django.contrib.auth.models import User

SEX_CHOICES = [
    ('O', '其他'), 
    ('B', '男'),
    ('G', '女'),
]

STATUS_CHOICES = [
    ('Y', '未入社'), 
    ('M', '已入社'),
    ('NP', '未付款'),
]

class Position(models.Model):
    """
    社員職位:
        社員
        幹部
    """
    name = models.CharField(max_length=15)

    def __str__(self):
        return "%s" % (self.name)

class Degree(models.Model):
    name = models.CharField(max_length=15, null=True)

    def __str__(self):
        return "%s" % (self.name)

class College(models.Model):
    name = models.CharField(max_length=15, null=True)
    degree = models.ForeignKey('Degree', on_delete=models.CASCADE)

    def __str__(self):
        return "[%s] %s" % (self.degree.name, self.name)

class Department(models.Model):
    name = models.CharField(max_length=20, null=True)
    college = models.ForeignKey('College', on_delete=models.CASCADE)

    def __str__(self):
        return "[%s] %s - %s" % (self.college.degree.name, self.college.name, self.name)

class Lesson(models.Model):
    name = models.CharField(max_length=15)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return "[%s] (%s) %s - %s" % (self.department.college.degree.name, self.department.college.name, self.department.name, self.name)

class Member(models.Model):
    """
    社員(包含幹部)
    活動參與者
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='memberuser')
    nid = models.CharField(max_length=15, unique=True) #學號
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, null=True, blank=True) #性別
    phone = models.CharField(max_length=15, null=True, blank=True, unique=True) #電話
    birthday = models.DateField(null=True, blank=True) #生日
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, null=True, blank=True) #系級
    positions = models.ForeignKey('Position', on_delete=models.CASCADE, null=True, blank=True) #職位
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default="Y") #狀態

    def __str__(self):
        return "%s [%s]" % (self.nid, self.get_status_display())

class Attendee(models.Model):
    """
    非在校學生
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="attendeeuser")
    nid = models.CharField(max_length=30, unique=True, null=True, blank=True) #學號
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, null=True, blank=True) #性別
    phone = models.CharField(max_length=15, null=True, blank=True, unique=True) #電話
    birthday = models.DateField(null=True, blank=True) #生日
    job = models.CharField(max_length=50, null=True, blank=True) #工作單位或學校系級
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default="Y") #狀態

    def __str__(self):
        return "%s [%s]" % (self.user.last_name+self.user.first_name, self.get_status_display()) 

