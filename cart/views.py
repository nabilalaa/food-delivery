from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser
from .models import *


def view_cart(request):

    if request.user != AnonymousUser():

        cart_items = CartItem.objects.filter(
            user=request.user).order_by("product__name")
        total_price = sum(item.product.price *
                          item.quantity for item in cart_items)
    else:
        return redirect("login")

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


def handelCart(request, meal_id):
    product = Item.objects.get(id=meal_id)
    quantity = request.POST.get("quantity")
    if request.user != AnonymousUser():

        cart_item, created = CartItem.objects.get_or_create(product=product,
                                                            user=request.user)
        cart_item.quantity = quantity
        cart_item.save()

        cart_items = CartItem.objects.filter(
            user=request.user).order_by("product__name")
        total_price = sum(item.product.price *
                          item.quantity for item in cart_items)

    else:
        return redirect("login")

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')
