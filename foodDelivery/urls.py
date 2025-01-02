from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('getmeal/<int:id>', getMeal, name="getMeal"),

    path('cart/', view_cart, name='view_cart'),
    path('handelcart/<int:meal_id>', handelCart, name='handelcart'),

    path('add/<int:meal_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),

    path('checkout/', checkout, name='checkout'),

]
