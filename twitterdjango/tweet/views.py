from django.shortcuts import render
from .models import Tweet


def tweetid(request, pk):
    html = 'twitterfeed.html'
    page_options = {}
    tweet = Tweet.objects.filter(pk=pk)
    page_options.update({"tweets": tweet})
    return render(request, html, page_options)
