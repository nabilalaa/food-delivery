from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser
from .models import *


def view_cart(request):


    cart_items = CartItem.objects.filter(
        cart__session_key=request.session.session_key).order_by("product__name")
    print(cart_items)
    total_price = sum(item.product.price *
                        item.quantity for item in cart_items)


    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


def handelCart(request, meal_id):
    product = Item.objects.get(id=meal_id)
    quantity = request.POST.get("quantity")
    cart, created = Cart.objects.get_or_create(session_key=request.session.session_key)

    cart_item, created = CartItem.objects.get_or_create(product=product,
                                                        cart=cart)
    cart_item.quantity = quantity
    cart_item.save()

    cart_items = CartItem.objects.filter(
        cart__session_key=request.session.session_key).order_by("product__name")
    total_price = sum(item.product.price *
                        item.quantity for item in cart_items)
    

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(cart__session_key=request.session.session_key,id=item_id)
    cart_item.delete()
    return redirect('view_cart')
