from django.db import models

class Job(models.Model):
    jobid = models.CharField(max_length=5, primary_key= True)
    jobtitle = models.CharField( max_length=30, null= False)
    minsal = models.IntegerField()

    def __str__(self):
        return self.jobid + " - "  + self.jobtitle

class Employee(models.Model):
    fullname = models.CharField(max_length=50)
    salary = models.IntegerField()
    job = models.ForeignKey(Job, on_delete = models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.fullname + " - "  + str(self.salary)

