from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    country = models.CharField(max_length=255, null=True, blank=True)
    place = models.CharField(max_length=255, null=True, blank=True)
    household_contact = models.CharField(max_length=255, null=True, blank=True)
