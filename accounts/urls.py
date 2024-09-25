from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name="home"),
    path('register', register, name="register"),
    path('login', user_login, name="login"),
    path('profile', profile, name="profile"),

    path('logout', user_logout, name="logout"),
    path('password_change', password_change, name="password_change"),


]
