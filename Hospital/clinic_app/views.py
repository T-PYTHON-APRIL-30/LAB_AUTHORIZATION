from django.shortcuts import render, redirect
from .models import Clinic, Appointment
from django.http import HttpRequest


# Create your views here.

def home(request):
    clinics = Clinic.objects.all()
    return render(request, 'clinic_app/home.html', {'clinics':clinics})

def add_clinic(request:HttpRequest):
    if request.method == 'POST':
        cname = request.POST['name']
        cfeature_image = request.POST['feature_image']
        cdescription = request.POST["description"]
        cdepartment = request.POST["department"]
        cestablished_at = request.POST["established_at"]
        new_clinic = Clinic(name=cname, feature_image=cfeature_image, description=cdescription, department=cdepartment, established_at=cestablished_at)
        new_clinic.save()
        return redirect('clinic_app:home') 
    else: 
        return render(request, 'clinic_app/add_clinic.html')