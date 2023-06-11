from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse

# Create your views here.

def signin(request:HttpRequest):
    msg = None
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('clinic_app:home')
        else:
            msg = "incorrect try again"
    return render(request, "accounts/signin.html", {"msg" : msg})

def signup(request:HttpRequest):
    if request.method == "POST":
        user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"], first_name=request.POST["first_name"], last_name=request.POST["last_name"])
        user.save()
        return redirect("clinic_app:home")
    return render(request, "accounts/signup.html")

def logout_view(request:HttpRequest):
    logout(request)
    return redirect("accounts:sign_in")