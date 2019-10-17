from django.db import models
from django.contrib.auth.models import User

from join.models import Member, Attendee
from add.models import Teacher, Location, Category

import os
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

class ActAttach(models.Model):
    """
    簡報或連結
    """
    name = models.CharField(max_length=50) #名稱
    url = models.URLField(max_length=200, null=True, blank=True) #網址
    file = models.FileField(upload_to='activity/', null=True, blank=True) #檔案
    desc = models.TextField(null=True, blank=True) #描述
    public = models.BooleanField(default=True) #是否公開

    def __str__(self):
        return "%s [%s]" % (self.name, self.public)

@receiver(models.signals.post_delete, sender=ActAttach)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `ActAttach` object is deleted.
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)

@receiver(models.signals.pre_save, sender=ActAttach)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `ActAttach` object is updated
    with new file.
    """
    if not instance.pk:
        return False
    try:
        old_file = ActAttach.objects.get(pk=instance.pk).file
    except Attach.DoesNotExist:
        return False

    new_file = instance.file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path) 

class Activity(models.Model):
    """
    活動
    """
    STATUS_CHOICES = [
        ('SINGUPYET', '尚未開始報名'),
        ('YET', '尚未開始'),
        ('FULL', '報名額滿'),
        ('SINGUPEND', '報名結束'),
        ('END', '活動結束'),
        ('HIDE', '隱藏'),
    ]

    name = models.CharField(max_length=50, unique=True) #名稱
    startdate = models.DateField() #開始日期
    endtdate = models.DateField() #結束日期
    starttime = models.TimeField() #開始時間
    endtime = models.TimeField() #結束時間
    teachers = models.ManyToManyField(Teacher) #講師(多個)
    attachs = models.ManyToManyField(ActAttach, null=True, blank=True) #簡報或檔案(多個)
    signup = models.URLField(max_length=200, null=True, blank=True) #報名連結
    locations = models.ForeignKey(Location, on_delete=models.CASCADE) #地點
    intro = models.TextField(null=True, blank=True)#簡介
    other = models.TextField(null=True, blank=True) #其他事項
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="HIDE")

    attendees = models.ManyToManyField(Attendee, null=True, blank=True) #參與者(非在校學生)
    members = models.ManyToManyField(Member, null=True, blank=True) #參與社員、參與者(在校學生)

    categorys = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s [%s]" % (self.name, self.get_status_display()) 
