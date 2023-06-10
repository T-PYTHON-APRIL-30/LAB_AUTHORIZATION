from django.shortcuts import render, redirect
from .models import Clinic, Appointment
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    clinics = Clinic.objects.all()
    return render(request, 'clinic_app/home.html', {'clinics':clinics})