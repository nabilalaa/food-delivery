from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CheckoutForm
from django.contrib import messages
from cart.models import *
from .models import *



def index(request):

    return render(request,"index.html")


def menu(request,name):
    

    category = request.POST.get("category")
    search = request.POST.get("search")

    if request.user.username== name : 
        if search:
            meals = Item.objects.filter(name__icontains=search,user__username=name)

        elif category and request.user.username== name:
            meals = Item.objects.filter(category__name=str(category).strip(),user__username=name)
            print(category)
        else:
            meals = Item.objects.filter(user__username=name)
    else:
        return HttpResponseRedirect("/admin")
        

    
    # if request.user.is_authenticated and name == request.user.username:

    cart_items = CartItem.objects.filter(cart__session_key=request.session.session_key)
    cart_items_length = sum(item.quantity for item in cart_items)
        # print(cart_items_length)
    # else:
    #     cart_items_length = "0"

    context = {
        "meals": meals or [],
        "cart": cart_items_length,
        "categories": Category.objects.filter(user__username=name) 

    }

    return render(request, "menu.html", context)


def getMeal(request, id):
    meal = Item.objects.get(id=id)
    context = {
        "meal": meal
    }
    return render(request, "modal.html", context)


# def view_cart(request):

#     if request.user != AnonymousUser():

#         cart_items = CartItem.objects.filter(
#             user=request.user).order_by("product__name")
#         total_price = sum(item.product.price *
#                           item.quantity for item in cart_items)
#     else:
#         return redirect("login")

#     return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


def add_to_cart(request, meal_id):
    product = Item.objects.get(id=meal_id)

    current_url = request.META.get("HTTP_REFERER", "")
    name = current_url.split("/menu/")[-1].strip("/")

    # print(name)
    if not request.session.session_key:
        request.session.create()
    cart, created = Cart.objects.get_or_create(session_key=request.session.session_key)
    cart_item, created = CartItem.objects.get_or_create(product=product,
                                                cart=cart)
    print(created)
    cart_item.quantity += 1
    cart_item.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
    # return HttpResponseRedirect(request.path_info)
    

# def handelCart(request, meal_id):
#     product = Item.objects.get(id=meal_id)
#     quantity = request.POST.get("quantity")
#     if request.user != AnonymousUser():

#         cart_item, created = CartItem.objects.get_or_create(product=product,
#                                                             user=request.user)
#         cart_item.quantity = quantity
#         cart_item.save()

#         cart_items = CartItem.objects.filter(
#             user=request.user).order_by("product__name")
#         total_price = sum(item.product.price *
#                           item.quantity for item in cart_items)

#     else:
#         return redirect("login")

#     return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


# def remove_from_cart(request, item_id):
#     cart_item = CartItem.objects.get(id=item_id)
#     cart_item.delete()
#     return redirect('view_cart')


def checkout(request):
    cart_items = CartItem.objects.filter(
        cart__user=request.user).order_by("product__name")
    total_price = sum(item.product.price *
                      item.quantity for item in cart_items)

    orders = []
    for i in (cart_items.values()):
        meal = Item.objects.get(id=i.get("product_id")).name
        qunatity = i.get("quantity")
        orders.append(f"{meal} X {qunatity}")
    o = "\n".join(orders)

    if request.method == "POST":
        form = CheckoutForm(request.POST)

        if form.is_valid():
            Order.objects.create(
                name=form.cleaned_data["name"], address=form.cleaned_data["address"],
                city=form.cleaned_data["city"], phone=form.cleaned_data["phone"], email=form.cleaned_data[
                    "email"], notes=form.cleaned_data["notes"], products=(o),user=request.user)
            messages.success(request, "sent successfully")
        else:
            print("error")

    context = {
        "form": CheckoutForm,
        "orders": CartItem.objects.filter(cart__user=request.user),
        "total": total_price
    }
    return render(request, "checkout.html", context)
