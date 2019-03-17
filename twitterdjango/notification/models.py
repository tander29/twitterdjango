from django.db import models
from twitterdjango.tweet.models import Tweet
from twitterdjango.twitteruser.models import TwitterUser


class Notification(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    to_user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    has_seen = models.BooleanField(default=False)
