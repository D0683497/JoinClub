from django.db import models

class Teacher(models.Model):
    """
    講師
    """
    first_name = models.CharField(max_length=30) #名字
    last_name = models.CharField(max_length=150) #姓氏
    job = models.TextField(null=True, blank=True) #現職
    exp = models.TextField(null=True, blank=True) #學經歷
    other = models.TextField(null=True, blank=True) #其他

    def __str__(self):
        return "%s" % (self.last_name+self.first_name) 

class Location(models.Model):
    """
    地點
    """
    name = models.TextField()
    way = models.TextField(null=True, blank=True) #路徑

    def __str__(self):
        return "%s" % (self.name) 

class Category(models.Model):
    """
    社課、講座分類
    """
    name = models.CharField(max_length=50, unique=True) #名稱

    def __str__(self):
        return "%s" % (self.name) 
