from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    displayname = models.CharField(max_length=15)
    date_created = models.TimeField()
    bio = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField('self', symmetrical=False)
