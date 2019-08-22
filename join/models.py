from django.db import models

LEVEL_CHOICES = [
    ('B1', 'freshman'), #大一
    ('B2', 'sophomore'), #大二
    ('B3', 'junior'), #大三
    ('B4', 'senior'), #大四
    ('M1', 'first year of graduate school'), #碩一
    ('M2', 'second year of graduate school'), #碩二
]

STATUS_CHOICES = [
    ('UR', 'under review'), #審核中
    ('M', 'member'), #社員
    ('NP', 'non-payment'), #未付款
]

class Member(models.Model):
    name = models.CharField(max_length=50)
    nid = models.CharField(max_length=15, unique=True)
    dept = models.CharField(max_length=20)
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default="UR")

    def __str__(self):
        return "%s [%s]" % (self.nid, self.get_status_display())