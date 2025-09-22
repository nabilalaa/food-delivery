from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),

    path('menu/<str:name>', menu, name="menu"),
    path('getmeal/<int:id>', getMeal, name="getMeal"),

    path('add/<int:meal_id>/', add_to_cart, name='add_to_cart'),
    path('checkout/', checkout, name='checkout'),

]
