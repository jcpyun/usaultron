from __future__ import unicode_literals

from django.db import models
import os

# Create your models here.
class ManifestData(models.Model):
    query=models.CharField(max_length=200)
   
    def __unicode__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=200)
    file = models.FileField(null=True, blank=True)
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title
    def filename(self):
        return os.path.basename(self.file.name)



# Create your models here.
class PolicePost(models.Model):
    Victim=models.CharField(max_length=200)
    Suspect=models.CharField(max_length=200)
    Longitude=models.CharField(max_length=200)
    Latitude=models.CharField(max_length=200)
    Information=models.TextField(blank=True, null=True)
    def __unicode__(self):
        return self.Suspect
    def __str__(self):
        return self.Suspect
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in PolicePost._meta.fields]
class ObjectPost(models.Model):
    Name= models.CharField(max_length=200)
    Age= models.DecimalField(max_digits=3,decimal_places=0)
    # Sex= models.CharField(max_length=10)
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    Sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    Birthday = models.DateField(null=True, blank=True)
    Address= models.CharField(max_length=200)
    Relations=models.CharField(max_length=300)
    def __unicode__(self):
        return self.Name
    def __str__(self):
        return self.Name
    
