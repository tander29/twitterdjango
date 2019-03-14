from django.urls import path
from twitterdjango.userprofile import views

urlpatterns = [
    path('', views.home, name='home')
]
