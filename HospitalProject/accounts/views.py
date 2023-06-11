from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def sign_up(request: HttpRequest):
    msg = None
    if request.method == "POST":
        try:
            user = User.objects.create_user(first_name=request.POST["first_name"], last_name=request.POST["last_name"], username=request.POST["username"], email=request.POST["email"], password=request.POST["password"])
            user.save()
            return redirect("accounts:sign_in")
        except:
            msg = "This username is taken"

    return render(request, "accounts/signup.html", {"msg" : msg})



def sign_in(request:HttpRequest):
    msg = None


    if request.method == "POST":
        user : User = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user:
            login(request, user)
            return redirect("hospital_app:home_page")
        else:
            msg = "Incorrect Credentials"


    return render(request, "accounts/signin.html", {"msg" : msg})


def log_out(request: HttpRequest):

    logout(request)

    return redirect("hospital_app:home_page")


def no_permission_page(request: HttpRequest):


    return render(request, "accounts/no_permission.html")