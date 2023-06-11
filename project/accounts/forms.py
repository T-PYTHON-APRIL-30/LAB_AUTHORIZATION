from django import forms
from .models import * 
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username" , "password")


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username" , "email")


