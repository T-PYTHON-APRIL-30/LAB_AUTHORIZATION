
from .forms import *
from django.contrib.auth import authenticate , login
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render ,redirect
from django.db.models import Q
from .forms import LoginForm  

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password2']
            user = authenticate(request , username=username , password=password)
            if user is not None:
                login(request , user)
                return redirect('main_app:home')    
    else:
        form =UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form' : form ,})

def user_login(request):

    if request.method == 'POST':
        login_form = UserForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request , user)
            return redirect('main_app:home')
    else:
        login_form = UserForm() 
    return render(request , 'registration/login.html' , {
        'login_form' : login_form })

def logout(request):
    auth.logout(request)
    return redirect('accounts:login')


