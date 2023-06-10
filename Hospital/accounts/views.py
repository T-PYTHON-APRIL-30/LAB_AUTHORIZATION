from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
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
            return redirect('accounts:signin')
    return render(request, "accounts/signin.html", {"msg" : msg})

def logout(request:HttpRequest):
    logout(request)
    return redirect("clinic_app:home")