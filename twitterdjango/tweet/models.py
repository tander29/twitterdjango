from twitterdjango.twitteruser.models import TwitterUser
from django.db import models


class Tweet(models.Model):
    body = models.CharField(max_length=140)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    userprofile = models.ForeignKey(
        TwitterUser, on_delete=models.CASCADE)


