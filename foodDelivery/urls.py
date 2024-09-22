from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('getmeal/<int:id>', getMeal, name="getMeal"),
]
