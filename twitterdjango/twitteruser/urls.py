from django.urls import path
from twitterdjango.twitteruser import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_view, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('<username>', views.profile_view, name='profile')
]
