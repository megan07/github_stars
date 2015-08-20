from django.db import models


# GitHub Model
class Github(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    num_stars = models.IntegerField()
    num_watchers = models.IntegerField()
    num_forks = models.IntegerField()

    def __unicode__(self):
        return u'%s'%(self.name)