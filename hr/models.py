from django.db import models

# Create your models here.

class Job(models.Model):
    jobid = models.CharField(max_length=5, primary_key= True)
    jobtitle = models.CharField( max_length=30, null= False)
    minsal = models.IntegerField()

