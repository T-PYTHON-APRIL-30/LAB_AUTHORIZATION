from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

# Create your views here.

def sign_in(request:HttpRequest):
    
    return render(request,"accounts/sign_in.html")

def register(request:HttpRequest):
    
    return render(request,"accounts/register.html")

def log_out(request:HttpRequest):
    logout(request)
    return redirect("clinics_app:home_page")