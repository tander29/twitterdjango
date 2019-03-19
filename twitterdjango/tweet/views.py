from django.shortcuts import render, reverse, HttpResponseRedirect
from .models import Tweet
from operator import attrgetter
from .forms import TweetForm
from django.contrib.auth.decorators import login_required
from twitterdjango.notification.views import notification_check
from twitterdjango.notification.views import find_user_notifications
from twitterdjango.twitteruser.helpers import user_info

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


@login_required(login_url='/login')
def to_tweet_view(request):
    html = 'tweet.html'
    form = TweetForm()
    page_options = {"form": form}
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            this_tweet = Tweet.objects.create(
                body=data['body'],
                userprofile=request.user.twitteruser
            )
            notification_check(this_tweet)
        return HttpResponseRedirect(reverse('home'))
    page_options.update(find_user_notifications(request))
    page_options.update(user_info(request.user.twitteruser))

    return render(request, html, page_options)
