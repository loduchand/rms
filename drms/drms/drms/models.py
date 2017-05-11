from django.contrib.auth.models import Permission, User
from django.db import models
from datetime import datetime
from django.utils import timezone

class BuildJob(models.Model):
    #spec_id =models.ForeignKey(User, default=1)
    job_name = models.CharField(max_length=250)
    product_name = models.CharField(max_length=250)
    #lastSuccessfulBuild = models.DateTimeField(default=timezone.now)
    #lastUnsuccessfulBuild = models.DateTimeField(default=timezone.now)
    #lastAbortedBuild = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.job_name