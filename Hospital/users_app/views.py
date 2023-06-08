from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register_page(request: HttpRequest):
    return render(request, 'users_app/register.html')


def login_page(request: HttpRequest):
    return render(request, 'users_app/login.html')


def logout_page(request: HttpRequest):
    logout(request)

    return redirect('main_app:home_page')
