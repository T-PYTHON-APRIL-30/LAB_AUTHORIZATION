from django.shortcuts import render, redirect
from .models import Clinic, Appointment
from django.http import HttpRequest
from django.contrib.auth.models import User

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
    
def clinic_details(request:HttpRequest, clinic_id):
    clinic = Clinic.objects.get(id=clinic_id)
    try:
        if request.method == "POST":
            pass 
    except:
        return render(request, 'clinic_app/no_clinic.html')
    return render(request, 'clinic_app/clinic_details.html', {"clinic":clinic})

def search(request:HttpRequest):
    search_results = request.GET.get("search", "")
    clinic = Clinic.objects.filter(name__contains=search_results)
    return render(request, "clinic_app/search.html", {"clinics":clinic})

def update_clinic(request:HttpRequest, clinic_id):
    clinic = Clinic.objects.get(id=clinic_id)
    if request.method == "POST":
        clinic.name = request.POST['name']
        clinic.feature_image = request.FILES['feature_image']
        clinic.description = request.POST["description"]
        clinic.department = request.POST["department"]
        clinic.established_at = request.POST["established_at"]
        clinic.save()
        return redirect("clinic_app:clinic_details", clinic_id=clinic.id)
    else:
        return render(request, 'clinic_app/update_clinic.html', {"clinic":clinic})
    
def contact(request):
    return render(request, 'clinic_app/contact.html')

def appointment_page(request:HttpRequest, clinic_id):
    clinic = Clinic.objects.get(id=clinic_id)
    appointments = Appointment.objects.filter(clinic=clinic).order_by('appointment_datetime')
    return render(request, 'clinic_app/appointment.html', {'clinic': clinic, 'appointments': appointments})

def create_appointment(request:HttpRequest, clinic_id):
    clinic = Clinic.objects.get(id=clinic_id)
    if request.method == 'POST':
        Acase_description = request.POST['case_description']
        Apatient_age = request.POST['patient_age']
        Aappointment_datetime = request.POST["appointment_datetime"]
        new_appointment = Appointment(user=request.user, clinic=clinic, case_description=Acase_description, patient_age=Apatient_age, appointment_datetime=Aappointment_datetime)
        new_appointment.save()
        return redirect('clinic_app:appointment', clinic_id=clinic.id)
    return render(request, 'clinic_app/create_appointment.html', {"clinic":clinic})
