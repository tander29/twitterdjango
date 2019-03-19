from twitterdjango.tweet.models import Tweet


def user_info(user):
    """Return user options declutters view function"""
    page_options = {}
    if user:
        user_tweets = Tweet.objects.filter(userprofile=user.pk)
        following_count = len(user.following.all())
        page_options = {"username": user.username,
                        "tweet_count": len(user_tweets),
                        "tweets": user_tweets,
                        "following_count": following_count,
                        "user": user}

    return page_options


def follow_toggle(request, otheruser):
    """Toggle options for following used in Profile View """

    logged_in_user = request.user.twitteruser
    if otheruser not in logged_in_user.following.all():
        is_following = False
        submit_value = "Follow"
        action = logged_in_user.following.add
    if otheruser in logged_in_user.following.all():
        is_following = True
        submit_value = "UnFollow"
        action = logged_in_user.following.remove

    return {"otheruser": otheruser, "is_following": is_following,
            'submit_value': submit_value, "action": action}
