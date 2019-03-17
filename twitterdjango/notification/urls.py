from django.urls import path
from twitterdjango.notification import views


urlpatterns = [
    path('notification', views.notification, name='notification'),
]
