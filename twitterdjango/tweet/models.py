from twitterdjango.userprofile.models import UserProfile
from django.db import models


class Tweet(models.Model):
    body = models.CharField(max_length=280)
    date_created = models.TimeField()
    userprofile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE)
