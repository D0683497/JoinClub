from django.db import models

class Status(models.Model):
    name = models.CharField(max_length=50) #名稱

    def __str__(self):
        return "%s" % (self.name)

class Tea(models.Model):
    """
    茶會事前調查
    """
    nid = models.CharField(max_length=15, unique=True) #學號
    first_name = models.CharField(max_length=50, null=True, blank=True) # 名
    last_name = models.CharField(max_length=50, null=True, blank=True) # 姓
    status = models.ManyToManyField(Status) #狀態

    def __str__(self):
        return "%s" % (self.nid)


