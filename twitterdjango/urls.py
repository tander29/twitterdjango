"""twitterdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
# from django.urls import path
from twitterdjango.tweet.models import Tweet
from twitterdjango.twitteruser.models import TwitterUser
from twitterdjango.notification.models import Notification
from twitterdjango.twitteruser.urls import urlpatterns as twitteruserurls
from twitterdjango.tweet.urls import urlpatterns as tweeturls
from twitterdjango.notification.urls import urlpatterns as notificationurls
from django.conf import settings
from django.conf.urls.static import static

admin.site.register(Tweet)
admin.site.register(TwitterUser)
admin.site.register(Notification)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns += notificationurls
urlpatterns += tweeturls
urlpatterns += twitteruserurls


# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,
#                           document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL,
#                       document_root=settings.MEDIA_ROOT)
