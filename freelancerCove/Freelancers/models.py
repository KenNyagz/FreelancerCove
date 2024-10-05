from django.db import models
from django.utils import timezone

class freelancer(models.Model):
    """Template for freelancer object"""
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phone_no = models.IntegerField(null=True)
    joined = models.DateField(default=timezone.now)
    specialty = models.CharField(max_length=255)
    technologies = models.CharField(max_length=255)