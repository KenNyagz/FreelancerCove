from django.db import models
from django.utils import timezone

class Hirer(models.Model):
    '''Data template for hiring parties'''
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email_address = models.EmailField(max_length=255, unique=True)
    hashed_password = models.CharField(max_length=128, default=' ')
    phone_no = models.IntegerField(null=True)
    joined = models.DateField(default=timezone.now)