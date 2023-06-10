from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse

# Create your views here.

def signin(request:HttpRequest):
    msg = None
    if request == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('clinic_app:home')
        else:
            msg = "Incorrect Try Again"
    return render(request, "accounts/signin.html", {"msg" : msg})

def signup(request:HttpRequest):
    if request.method == "POST":
        user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"], first_name=request.POST["name"])
        user.save()
        return redirect("accounts:signin")
    return render(request, "accounts/signup.html")

def logout(request:HttpRequest):
    logout(request)
    return redirect("clinic_app:home") # to the signin? or home?