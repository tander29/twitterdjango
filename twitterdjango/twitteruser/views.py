from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import NewUser, Login
from .models import User, TwitterUser
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from twitterdjango.tweet.models import Tweet
from twitterdjango.notification.views import notification_check
from twitterdjango.notification.views import find_user_notifications
from twitterdjango.tweet.views import find_following_tweets
from twitterdjango.tweet.forms import TweetForm
from django.contrib.auth import logout
from twitterdjango.twitteruser.helpers import follow_toggle, user_info


@login_required(login_url='/login')
def home(request):
    """User home page where active_user can tweet and see own+following tweets"""
    user_id = request.user.twitteruser.pk
    follow_list = request.user.twitteruser.following.all()
    tweets = find_following_tweets(user_id, follow_list)
    form = TweetForm()
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            this_tweet = Tweet.objects.create(
                body=data['body'],
                userprofile=request.user.twitteruser
            )
            notification_check(this_tweet)
        return HttpResponseRedirect(reverse('home'))

    page_options = {"following_count": len(follow_list),
                    "tweet_count": tweets['tweet_count'],
                    "tweets": tweets['tweets'],
                    "form": form}
    page_options.update(find_user_notifications(request))
    return render(request, 'home.html', page_options)


def login_view(request):
    """Log in view on own page """
    html = 'home.html'
    form = Login()
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'], password=data['password'])

        if user:
            login(request, user)
            return HttpResponseRedirect(request.GET.get('next', '/'))
    return render(request, html, {"form": form})


def register(request):
    """Register new user """
    html = 'home.html'
    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'],
                password=data['password'],
                email=data['email']
            )
            login(request, user)
            TwitterUser.objects.create(
                user=user,
                bio=data['bio'],
                username=data['username'],
            )
            return HttpResponseRedirect(reverse('home'))
    form = NewUser()
    return render(request, html, {"form": form})


def profile_view(request, username):
    """See a users profile"""
    html = 'profile.html'
    user_exist = TwitterUser.objects.filter(username=username).first()
    page_options = {}
    if request.user.is_active and user_exist:
        follow_options = follow_toggle(request, user_exist)
        page_options.update({"is_following": follow_options['is_following'],
                             "submit_value": follow_options['submit_value']})
    if request.method == 'POST':
        follow_options['action'](user_exist)
        page_options.update({"is_following": follow_options['is_following'],
                             "submit_value": follow_options['submit_value']})
        return HttpResponseRedirect(user_exist.username)

    if user_exist:
        page_options.update(user_info(user_exist))
        if request.user.is_active:
            page_options.update(find_user_notifications(request))
        return render(request, html, page_options)
    else:
        return render(request, html)


def logout_view(request):
    """Log Out"""
    logout(request)
    return HttpResponseRedirect(reverse('home'))
