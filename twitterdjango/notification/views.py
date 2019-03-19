from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from twitterdjango.twitteruser.models import TwitterUser
from .models import Notification
import re
from twitterdjango.twitteruser.helpers import user_info


@login_required(login_url='../login')
def notification(request):
    html = 'notification.html'
    page_options = {}
    notifications = request.user.twitteruser.notification_set.get_queryset().all()
    tweets = []
    for notice in notifications:
        if not notice.has_seen:
            tweets += [notice.tweet]
            Notification.objects.filter(pk=notice.pk).update(has_seen=True)
    page_options.update(user_info(request.user.twitteruser))
    page_options.update({"tweets": tweets})
    page_options.update(find_user_notifications(request))
    print(page_options)
    return render(request, html, page_options)


def notification_check(tweet):
    """Used when creating new tweet"""
    notifications = re.findall(r"(@\w+)", tweet.body)
    if notifications:
        for person in notifications:
            user_to_notify = TwitterUser.objects.filter(
                username=person[1:]).first()
            if user_to_notify:
                Notification.objects.create(
                    tweet=tweet,
                    to_user=user_to_notify
                )
        return HttpResponseRedirect(reverse('home'))


def find_user_notifications(request):
    """Return this to update page options"""
    notifications = request.user.twitteruser.notification_set
    new_notification = 0
    for notice in notifications.get_queryset().all():
        if not notice.has_seen:
            new_notification += 1
    return {"notification": new_notification}
