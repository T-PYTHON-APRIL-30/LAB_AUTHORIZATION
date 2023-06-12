from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.contrib import auth
from .forms import LoginForm
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm


def user_signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1']) 
            new_user.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                # To get username for message
                username = form.cleaned_data['username'] 
                messages.success(
                    request, 'Congratulations {} Registration has been completed successfully .'.format(username)
                )
            return redirect('main_app:home')
    else:
        form = UserCreationForm()
    return render(request , 'registration/signup.html' ,  {
    'form' : form ,
    })

def user_login(request):
    if request.method == 'POST':
        form = LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username , password=password)
        if user is not None :
            login(request , user)
            return redirect('main_app:home')
    else:
        form = LoginForm()
    return render(request , 'registration/login.html' ,  {
        'form' : form , 
    })

def logout(request):
    auth.logout(request)
    return redirect('users:login')