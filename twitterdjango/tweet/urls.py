from django.urls import path
from twitterdjango.tweet import views


urlpatterns = [
    path('tweet/<int:pk>/', views.tweetid, name='tweetid'),
    path('tweet', views.to_tweet_view, name="tweet")
]
