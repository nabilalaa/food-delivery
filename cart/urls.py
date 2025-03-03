from django.urls import path
from .views import *
urlpatterns = [
    path('cart/', view_cart, name='view_cart'),
    path('handelcart/<int:meal_id>', handelCart, name='handelcart'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),

]
