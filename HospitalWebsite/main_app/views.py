from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Clinic ,Appointment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime

# Create your views here.


def home_page(request:HttpRequest):
    clinics=Clinic.objects.all().order_by('established_at')
    return render(request, "main_app/home.html",{'clinics':clinics})

def about_us(request:HttpRequest):
    return render(request,'main_app/about_us.html')


 #Clinics Views   

def add_clinics(request:HttpRequest):
    if not (request.user.is_staff and  request.user.has_perm("main_app.add_clinic")):
        return redirect("accounts:no_permission_page")
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        feature_image=request.FILES['feature_image']
        established_at = request.POST['established_at']
        department=request.POST['department']
        clinc_object = Clinic.objects.create(name=name, department=department,description=description, established_at=established_at, feature_image=feature_image)
        clinc_object.save()
        return redirect('main_app:home_page')
    else:
        
        return render(request, "main_app/add_clinics.html", {'department_choices': Clinic.DEPARTMENT_CHOICES})
    

def clinic_detail(request:HttpRequest,clinic_id):
    clinic=Clinic.objects.get(id=clinic_id)
    return render(request, "main_app/clinic_detail.html", {'clinic':clinic})


def update_clinics(request:HttpRequest, clinic_id):
    if not (request.user.is_staff and  request.user.has_perm("main_app.change_clinic")):
        return redirect("accounts:no_permission_page")
    clinic=Clinic.objects.get(id=clinic_id)
    iso_date = clinic.established_at.isoformat()

    if request.method == "POST":
        clinic.name = request.POST['name']
        clinic.description = request.POST['description']
        clinic.feature_image=request.FILES['feature_image']
        clinic.established_at = request.POST['established_at']
        clinic.department=request.POST['department']
        if "feature_image" in request.FILES:
            clinic.feature_image=request.FILES["feature_image"]
        clinic.save()
        return redirect('main_app:clinic_detail',clinic_id=clinic.id)
    else:
        
        return render(request, "main_app/update_clinics.html", {'department_choices': Clinic.DEPARTMENT_CHOICES,'clinic':clinic,'iso_date':iso_date})
    
def search_page(request:HttpRequest):
    search_phrase = request.GET.get("search", "")
    clinic = Clinic.objects.filter(name__contains=search_phrase)

    return render(request, "main_app/search_page.html", {"clinics" : clinic})


#Appointment Views

def create_appointment(request:HttpRequest,clinic_id): 
    clinic = Clinic.objects.get(id=clinic_id)
    if request.method == 'POST':
        
        appointment_datetime_str = request.POST.get('appointment_datetime').replace('T', ' ')
        appointment_datetime = timezone.make_aware(datetime.datetime.strptime(appointment_datetime_str, '%Y-%m-%d %H:%M'))
       
        if not clinic.is_available(appointment_datetime):
            messages.error(request, 'Clinic is not available at the specified time.')
            return redirect('main_app:create_appointment', clinic_id=clinic.id)
        
        appointment = Appointment(clinic=clinic, user= request.user ,appointment_datetime=appointment_datetime,case_description=request.POST['case_description'],patient_age=request.POST['patient_age'])
        appointment.save()
        messages.success(request, 'Appointment created successfully.')
        return redirect('main_app:appointment_list')
    else:
        available_times = clinic.get_available_times()
        return render(request, 'main_app/create_appointment.html', {'clinic': clinic ,'available_times': available_times })

#-----------------------------------



def appointment_list(request:HttpRequest):
    
    if not (request.user.is_staff and  request.user.has_perm("main_app.add_appointment")):
        appointment_user=Appointment.objects.filter(user=request.user)
    else:
        appointment_user=Appointment.objects.all()
    return render(request,"main_app/appointment_list.html",{"appointment_user":appointment_user })
    


def delete_appointment(request:HttpRequest, appointment_id):
    if not (request.user.is_staff and  request.user.has_perm("main_app.delete_appointment")):
        return redirect("accounts:no_permission_page")
    
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.delete()

    return redirect('main_app:appointment_list')


#---------

def update_appointment(request:HttpRequest, appointment_id):
    if not (request.user.is_staff and  request.user.has_perm("main_app.change_appointment")):
        return redirect("accounts:no_permission_page")
    appointment=Appointment.objects.get(id=appointment_id)
    iso_date = appointment.appointment_datetime.isoformat()

    if request.method == "POST":
        appointment.patient_age = request.POST['patient_age']
        appointment.case_description = request.POST['case_description']
        appointment.appointment_datetime = request.POST['appointment_datetime']
        appointment.is_attended= bool(request.POST.get('is_attended', False))
        appointment.save()
        return redirect('main_app:appointment_list')
    else:
        
        return render(request, "main_app/update_appointment.html", {'appointment':appointment,'iso_date':iso_date})


         
    