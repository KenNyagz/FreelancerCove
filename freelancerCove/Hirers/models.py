from django.db import models
from django.utils import timezone

class Hirer(models.Model):
    '''Data template for hiring parties'''
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phone_no = models.IntegerField(null=True)
    joined = models.DateField(default=timezone.now)