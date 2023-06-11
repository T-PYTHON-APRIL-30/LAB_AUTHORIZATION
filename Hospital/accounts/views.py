from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def sign_up(request: HttpRequest):
    msg = None
    if request.method == "POST":
        try:
            user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"], first_name=request.POST["first_name"], last_name=request.POST["last_name"])
            user.save()
            return redirect("accounts:sign_in")
        except:
            msg = "Please choose another username!"

    return render(request, "accounts/signup.html", {"msg" : msg})



def sign_in(request:HttpRequest):
    msg = None

    if request.method == "POST":
        user : User = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user:
            login(request, user)
            return redirect("main_app:homePage")
        else:
            msg = "Incorrect username or password"


    return render(request, "accounts/signin.html", {"msg" : msg})


def log_out(request: HttpRequest):

    logout(request)

    return redirect("main_app:homePage")


def no_permission_page(request: HttpRequest):


    return render(request, "accounts/no_permission.html")