from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.http import JsonResponse
from django.core.serializers import serialize
from django.contrib.auth.models import AnonymousUser


from .models import *


def index(request):
    category = request.POST.get("category")
    search = request.POST.get("search")
    if search:
        meals = Meal.objects.filter(name__icontains=search)

    elif category:
        meals = Meal.objects.filter(category__name=category)

    else:
        meals = Meal.objects.all()

    if request.user != AnonymousUser():

        cart_items = CartItem.objects.filter(user=request.user)
        cart_items_length = sum(item.quantity for item in cart_items)
    else:
        return redirect("login")
    context = {
        "meals": meals,
        "cart": cart_items_length,
        "categories": Category.objects.all()

    }

    return render(request, "index.html", context)


def getMeal(request, id):
    meal = Meal.objects.get(id=id)
    context = {
        "meal": meal
    }
    return render(request, "modal.html", context)


def view_cart(request):

    if request.user != AnonymousUser():

        cart_items = CartItem.objects.filter(
            user=request.user).order_by("product__name")
        total_price = sum(item.product.price *
                          item.quantity for item in cart_items)
    else:
        return redirect("login")

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


def handelCart(request, meal_id):
    product = Meal.objects.get(id=meal_id)
    quantity = request.POST.get("quantity")
    print(quantity)
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
