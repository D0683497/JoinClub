from django.db import models

class Attend(models.Model):
    name = models.CharField(max_length=50)
    nid = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return "%s %s" % (self.nid, self.name)

