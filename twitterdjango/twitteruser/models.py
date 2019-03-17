from django.contrib.auth.models import User
from django.db import models


class TwitterUser(models.Model):
    username = models.CharField(max_length=15)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    bio = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField('self', symmetrical=False, blank=True)
