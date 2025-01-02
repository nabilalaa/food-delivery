from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import views


def index(request):
    return render(request, "index.html")


def register(request):
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    confirm_password = request.POST.get("confirm-password")

    try:
        if request.method == "POST":

            if password == confirm_password and User.DoesNotExist:
                User.objects.create_user(
                    username=username, email=email, password=password)
                messages.success(
                    request, message="register has been sucessfully")
                redirect("login")

            else:
                messages.error(request, message="somthing wrong")

    except:
        messages.error(request, message="username or email is exist ")

    return render(request, "register.html")


def user_login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        if (authenticate(request, username=username, password=password)):
            login(request, authenticate(
                request, username=username, password=password))
            messages.success(
                request, message="login has been sucessfully")
            return redirect("/")
        else:
            messages.error(request, message="username or password is invaild")

    return render(request, "login.html")


def user_logout(request):
    logout(request)

    return redirect("home")


def password_change(request):
    if not request.user.is_authenticated:
        return redirect("login")
    u = User.objects.get(username=request.user.username)
    password = request.POST.get("password")
    confirmPassword = request.POST.get("confirm-password")
    oldPassword = request.POST.get("old-password")

    if request.POST and u.check_password(oldPassword) and password == confirmPassword and password and confirmPassword and oldPassword:
        u.set_password(password)
        u.save()
        user_logout(request)
        return redirect("home")
    else:
        print("sss")
        messages.error(request, message="somthing wrong")
    return render(request, "password_change.html")


def profile(request):

    return render(request, "profile.html")
