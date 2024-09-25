from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.http import JsonResponse
from django.core.serializers import serialize
from django.contrib.auth.models import AnonymousUser


from .models import *


def index(request):

    search = request.POST.get("search")
    if search:
        meals = Meal.objects.filter(name__icontains=search)

    else:
        meals = Meal.objects.all()

    cart_items = CartItem.objects.all()
    cart_items_length = sum(item.quantity for item in cart_items)
    context = {
        "meals": meals,
        "cart": cart_items_length

    }

    return render(request, "index.html", context)


def getMeal(request, id):
    meal = Meal.objects.get(id=id)
    context = {
        "meal": meal
    }
    return render(request, "modal.html", context)


def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price *
                      item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


def add_to_cart(request, meal_id):
    product = Meal.objects.get(id=meal_id)

    if request.user != AnonymousUser():

        cart_item, created = CartItem.objects.get_or_create(product=product,
                                                            user=request.user)
        cart_item.quantity += 1
        cart_item.save()
        return redirect('home')
    else:
        return redirect("login")


def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')
