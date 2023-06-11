from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Clinic, Appointment

# Create your views here.

def home_page(request :HttpRequest):
    clinics = Clinic.objects.all()

    return render(request,"hospital_app/home.html",{"clinics":clinics})

def clinic_details(request :HttpRequest,clinic_id):
    clinic = Clinic.objects.get(id=clinic_id)
    
    if not (request.user.is_staff and request.user.has_perm("hospital_app.view_appointment")):
        appointment_user = Appointment.objects.filter(user=request.user, clinic=clinic)
    else:
        appointment_user = Appointment.objects.all()

    return render(request,"hospital_app/details.html",{'clinic':clinic, 'appointment_user':appointment_user})

def appointment_details(request :HttpRequest,appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    clinics = Clinic.objects.filter(appointment=appointment)
    
    return render(request,"hospital_app/appointment_details.html",{'appointment':appointment, 'clinics':clinics})

def add_clinic(request :HttpRequest):
    
    if request.method == "POST":
        new_clinic = Clinic( name = request.POST['name'],feature_image = request.FILES['feature_image'],description = request.POST['description'],department = request.POST['department'])
        new_clinic.save()
        return redirect("hospital_app:home_page")
    
    return render(request, "hospital_app/add_clinic.html", {"departmrnts" : Clinic.DEP_CHOICES})

def search_page(request:HttpRequest):
    search_phrase = request.GET.get("search", "")
    clinics = Clinic.objects.filter(name__contains=search_phrase)

    return render(request, "hospital_app/search_page.html", {"clinics" : clinics})

def update_clinic(request:HttpRequest, clinic_id):

    clinic = Clinic.objects.get(id=clinic_id)
    #updating the clinic
    if request.method == "POST":
        clinic.name = request.POST["name"]
        if "feature_image" in request.FILES:
            clinic.feature_image = request.FILES["feature_image"]
            
        clinic.description = request.POST["description"]
        clinic.department = request.POST["department"]
        clinic.save()

        return redirect("hospital_app:clinic_details", clinic_id=clinic.id)

    return render(request, 'hospital_app/update_clinic.html', {"clinic" : clinic, "departmrnts" : Clinic.DEP_CHOICES})

def update_appointment(request:HttpRequest, appointment_id):

    appointment = Appointment.objects.get(id=appointment_id)
    iso_date = appointment.appointment_datetime.isoformat()
    #updating the clinic
    if request.method == "POST":
        appointment.case_description = request.POST["case_description"]
        appointment.patient_age = request.POST["patient_age"]
        appointment.appointment_datetime = request.POST["appointment_datetime"]
        appointment.is_attended = request.POST["is_attended"]
        appointment.save()

        return redirect("hospital_app:appointment_details", appointment_id=appointment.id)

    return render(request, 'hospital_app/update_appointment.html', {"appointment" : appointment,"iso_date" : iso_date})

def delete_clinic(request:HttpRequest, clinic_id):

    #check that user is staff and has a permission to delete
    if not (request.user.is_staff and  request.user.has_perm("hospital_app.delete_clinic")):
        return redirect("accounts:no_permission_page")
    
    clinic = Clinic.objects.get(id=clinic_id)
    clinic.delete()

    return redirect("hospital_app:home_page")

def delete_appointment(request:HttpRequest, appointment_id):

    #check that user is staff and has a permission to delete
    if not (request.user.is_staff and  request.user.has_perm("hospital_app.delete_appointment")):
        return redirect("accounts:no_permission_page")
    
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.delete()

    return redirect("hospital_app:home_page")
        
def book_appointment(request:HttpRequest, clinic_id):

    if request.method == "POST":
        clinic_object = Clinic.objects.get(id=clinic_id)
        new_appointment = Appointment(clinic=clinic_object, user=request.user, case_description=request.POST["case_description"], patient_age=request.POST["patient_age"],appointment_datetime = request.POST['appointment_datetime'],is_attended = request.POST['is_attended'])
        new_appointment.save()

    
    return redirect("hospital_app:clinic_details", clinic_id=clinic_id)
        