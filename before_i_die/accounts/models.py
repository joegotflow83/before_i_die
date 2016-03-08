from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    origin = models.CharField(max_length=32)
    dream_location = models.CharField(max_length=32)
    age = models.IntegerField()
