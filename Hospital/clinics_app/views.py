from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse
from .models import Clinic , Appointment

# Create your views here.

# any user can access 
def home_page(request:HttpRequest):
    clinics = Clinic.objects.all()
    return render(request,"clinics_app/home_page.html",{"clinics":clinics})

def clinics_page(request:HttpRequest):
    clinics = Clinic.objects.all()
    return render(request,"clinics_app/clinics_page.html",{'clinics':clinics})

def about_page(request:HttpRequest):
    return render(request,"clinics_app/about_page.html")

def clinic_detail_page(request:HttpRequest,clinic_id):
    clinics = Clinic.objects.get(id = clinic_id)
    return render(request,"clinics_app/clinic_detail_page.html",{'clinics':clinics})

# ----------------------------------- Only manager's can access ----------------------------------- 

def manager_page(request:HttpRequest):
    return render(request,"clinics_app/manager_page.html")

# Appointment
def appointment_manager_page(request:HttpRequest):
    return render(request,"clinics_app/appointment_manager_page.html")

def add_appointment_page(request:HttpRequest):
    return render(request,"clinics_app/add_appointment_page.html")


# Clinics
def clinic_manager_page(request:HttpRequest):
    clinics = Clinic.objects.all()
    return render(request,"clinics_app/clinic_manager_page.html",{'clinics':clinics})

def add_clinic_page(request:HttpRequest):
    clinics = Clinic.objects.all()

    if request.method == "POST":
        if "image" in request.FILES:
            new_clinic = Clinic(clinic_name = request.POST["clinic_name"],
                                 description = request.POST["description"],department = request.POST["department"],
                                 established_at = request.POST["established_at"], feature_image = request.FILES["feature_image"])
        else:
            new_clinic = Clinic(clinic_name = request.POST["clinic_name"],
                                 description = request.POST["description"],department = request.POST["department"],
                                 established_at = request.POST["established_at"])
        new_clinic.save()
        return redirect("clinics_app:clinic_manager_page")
    
    return render(request,"clinics_app/add_clinic_page.html",{"clinics":clinics})

def add_clinic_page(request):
    clinics = Clinic.objects.all()
    
    if request.method == "POST":
        if "image" in request.FILES:
            new_clinic = Clinic(
                clinic_name=request.POST["clinic_name"],
                description=request.POST["description"],
                department=request.POST["department"],
                established_at=request.POST["established_at"],
                feature_image=request.FILES["image"]
            )
        else:
            new_clinic = Clinic(
                clinic_name=request.POST["clinic_name"],
                description=request.POST["description"],
                department=request.POST["department"],
                established_at=request.POST["established_at"]
            )
        
        new_clinic.save()
        return redirect("clinics_app:clinic_manager_page")
    
    return render(request, "clinics_app/add_clinic_page.html", {"clinics": clinics})

def update_clinic_page(request:HttpRequest,clinic_id):
    
    clinics = Clinic.objects.all()
    clinic = Clinic.objects.get( id = clinic_id )
    iso_date = clinic.established_at.isoformat()

    if request.method == "POST":
        clinic.clinic_name=request.POST["clinic_name"]
        clinic.description=request.POST["description"]
        clinic.department=request.POST["department"]
        clinic.established_at=request.POST["established_at"]
        if "image" in request.FILES:
            clinic.feature_image=request.FILES["image"]
        clinic.save()
        return redirect("clinics_app:clinic_manager_page")

    return render(request,"clinics_app/update_clinic_page.html",{"clinic":clinic,"iso_date":iso_date,"clinics":clinics})

def delete_clinic_page(request:HttpRequest, clinic_id):
    clinic = Clinic.objects.get(id = clinic_id) 
    clinic.delete()
    return redirect("clinics_app:clinic_manager_page")