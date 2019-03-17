from django.shortcuts import render
from .models import Tweet
from operator import attrgetter


"""Added ability to tweet on home page, didn't see the need to make it's own page"""


def tweetid(request, pk):
    """Renders a single tweet on own"""
    html = 'twitterfeed.html'
    page_options = {}
    tweet = Tweet.objects.filter(pk=pk)
    page_options.update({"tweets": tweet})
    return render(request, html, page_options)


def find_following_tweets(user_id, following):
    """searches users active user is following and finds there tweets """
    tweets = Tweet.objects.filter(userprofile=user_id).all()
    my_tweet_count = len(tweets)
    for user in following:
        tweets = tweets | Tweet.objects.filter(userprofile=user.pk).all()
    return {"tweets": sorted(tweets, key=attrgetter('date_created'),
                             reverse=True),
            "tweet_count": my_tweet_count}
