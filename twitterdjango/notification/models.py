from django.db import models
from twitterdjango.tweet.models import Tweet
from twitterdjango.userprofile.models import UserProfile


class Notification(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    to_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    has_seen = models.BooleanField()
