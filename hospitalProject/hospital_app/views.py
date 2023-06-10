from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Clinic,Appointment

# Create your views here.


def index_page(request:HttpRequest):
    clinics=Clinic.objects.all()
    
    return render(request,'hospital_app/index.html',{"clinics":clinics})


def add_clinics(request:HttpRequest):
    if not (request.user.is_staff and request.user.has_perm("hospital_app.add_clinic")):
        return redirect("hospital_app:no_permission_page")
    
    if request.method=="POST":
        new_clinic=Clinic(name=request.POST["name"],image=request.FILES["image"],description=request.POST["description"],department=request.POST["department"],established_at=request.POST["established_at"])

        new_clinic.save()
        return redirect("hospital_app:index_page")  
    return render(request,"hospital_app/add.html")



def detail_page(request:HttpRequest,clinic_id):
    try:
        clinic = Clinic.objects.get(id=clinic_id)
    except:
        return render(request, 'hospital_app/not_found.html')
    return render(request,"hospital_app/detail.html",{"clinic":clinic})


def delete_clinics(request:HttpRequest,clinic_id):
    if not (request.user.is_staff and request.user.has_perm("hospital_app.delete_clinics")):
        return redirect("hospital_app:no_permission_page")
    clinic = Clinic.objects.get(id=clinic_id)
    clinic.delete()
    return redirect("hospital_app:manager_page")
    

def update_page(request:HttpRequest ,clinic_id):
    if not (request.user.is_staff):
        return redirect("hospital_app:no_permission_page")
    clinic = Clinic.objects.get(id=clinic_id)
    iso_format= clinic.established_at.isoformat()
    if request.method=="POST":
        clinic.name=request.POST["name"]
        clinic.description=request.POST["description"]
        clinic.department=request.POST["department"]
        if "image" in request.FILES:
            clinic.image=request.FILES["image"]
        clinic.established_at=request.POST["established_at"]
        clinic.save()
        return redirect("hospital_app:manager_page")
    return render(request,"hospital_app/update.html",{"clinic":clinic,"iso_format":iso_format})

   
    
    

def search_page(request:HttpRequest):
   search_phrase = request.GET.get("search", "")
   clinics = Clinic.objects.filter(name__contains=search_phrase)
   return render(request, "hospital_app/search.html", {"clinics" : clinics})

def manager_page(request:HttpRequest):
    if not (request.user.is_staff):
        return redirect("hospital_app:no_permission_page")
    clinics=Clinic.objects.all()
    return render(request,"hospital_app/Manager.html",{"clinics":clinics})

def add_appointment(request:HttpRequest,clinic_id):
 
    clinic = Clinic.objects.get(id=clinic_id)
    msg=None
    if request.method=="POST":
        
        appointment=Appointment.objects.filter(clinic=clinic,appointment_datetime=request.POST["appointment_datetime"])
        if len(appointment)>0:
            msg="you cant take this time"
            return render(request,"hospital_app/add_appointment.html",{"clinic":clinic,"clinic_id":clinic_id ,"msg":msg})
            
        new_appointment=Appointment(clinic=clinic,user=request.user,case_description=request.POST["case_description"],patient_age=request.POST["patient_age"],appointment_datetime=request.POST["appointment_datetime"])
        
        new_appointment.save()
        return redirect("hospital_app:index_page")

    return render(request,"hospital_app/add_appointment.html",{"clinic":clinic,"clinic_id":clinic_id ,"msg":msg})
    
    
def view_appointment(request:HttpRequest,clinic_id):
    
    clinic = Clinic.objects.get(id=clinic_id)
    appointments=Appointment.objects.filter(user=request.user,clinic=clinic)
    return render(request,"hospital_app/view_appointment.html",{"appointments":appointments,"clinic":clinic})


def manage_appointment(request:HttpRequest,clinic_id):
    if not (request.user.is_staff):
        return redirect("hospital_app:no_permission_page")

    clinic = Clinic.objects.get(id=clinic_id)
    appointments=Appointment.objects.filter(clinic=clinic)
    return render(request,"hospital_app/manage_appointment.html",{"appointments":appointments,"clinic":clinic})





def delete_appointent(request:HttpRequest,appointment_id,clinic_id):
    appointment=Appointment.objects.get(id=appointment_id)
    appointment.delete()
    return redirect("hospital_app:manage_appointment",clinic_id)


def patient_attended(request:HttpRequest,appointment_id,clinic_id):
    appointment=Appointment.objects.get(id=appointment_id)
    appointment.is_attended=True
    appointment.save()
    return redirect("hospital_app:manage_appointment",clinic_id)

def patient_notattended(request:HttpRequest,appointment_id,clinic_id):
    appointment=Appointment.objects.get(id=appointment_id)
    appointment.is_attended=False
    appointment.save()
    return redirect("hospital_app:manage_appointment",clinic_id)
import datetime
def update_appointent(request:HttpRequest,appointment_id,clinic_id):
    appointment=Appointment.objects.get(id=appointment_id)
    clinic = Clinic.objects.get(id=clinic_id)
    new_format=appointment.appointment_datetime.strftime("%d-%m-%YT%H:%M")


    if request.method=="POST":
        appointment.case_description=request.POST["case_description"]
        if "appointment_datetime" in request.POST:
            appointment.appointment_datetime=request.POST["appointment_datetime"]
        appointment.patient_age=request.POST["patient_age"]
        appointment.save()
        return redirect("hospital_app:manage_appointment",clinic_id)
    return render(request,"hospital_app/update_appointment.html",{"clinic":clinic ,"appointment":appointment,"new_format":new_format})


from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def sign_up(request: HttpRequest):
    msg = None
    if request.method == "POST":
    
            user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"],  first_name=request.POST["name"])
            user.save()
            return redirect("hospital_app:sign_in")
    

    return render(request, "hospital_app/signup.html", {"msg" : msg})



def sign_in(request:HttpRequest):
    msg = None


    if request.method == "POST":
        user : User = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user:
            login(request, user)
            return redirect("hospital_app:index_page")
        else:
            msg = "Incorrect Credentials"


    return render(request, "hospital_app/signin.html", {"msg" : msg})


def log_out(request: HttpRequest):

    logout(request)

    return redirect("hospital_app:index_page")


def no_permission_page(request: HttpRequest):


    return render(request, "hospital_app/no_permission.html")