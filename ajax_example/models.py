from django.db import models

class item(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    def __unicode__(self):
        return self.name + " - " + self.type