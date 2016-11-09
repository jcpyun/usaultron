from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
# Create your models here.
class DashboardPost(models.Model):
    title=models.CharField(max_length=200)
    file = models.FileField(null=True, blank=True)
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title
