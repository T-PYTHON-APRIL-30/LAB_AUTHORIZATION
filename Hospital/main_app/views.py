from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Clinic, Appointment, User

# Create your views here.

def homePage (request:HttpRequest):
    if request.user.is_authenticated:
        print(request.user.first_name)

    clinics = Clinic.objects.all()

    return render(request, "main_app/home.html", {"clinics" : clinics})

def addClinic (request:HttpRequest):

    if not request.user.is_staff:
        return redirect("accounts:no_permission_page")

    appointments = Appointment.objects.all()

    if request.method == "POST":
        #addin a new clinic in database
        #appointment = Appointment.objects.get(id=request.POST["appointment"])
        new_clinic = Clinic(name=request.POST["name"], feature_image=request.FILES["feature_image"], description=request.POST["description"], department=request.POST["department"])
        new_clinic.save()
        return redirect("main_app:homePage")

    return render(request, "main_app/add_clinic.html")

def clinic_detail(request:HttpRequest, clinic_id):

    try:
        clinic = Clinic.objects.get(id=clinic_id)
        appointments = Appointment.objects.filter(clinic=clinic)
    except:
        return render(request, 'main_app/not_found.html')

    return render(request, 'main_app/clinic_details.html', {"clinic" : clinic, "appointments" : appointments})
                  

def update_clinic(request:HttpRequest,clinic_id):
    clinic = Clinic.objects.get(id=clinic_id)
    iso_date = clinic.established_at.isoformat()

    appointments = Appointment.objects.all()


    #updating the clinic
    if request.method == "POST":
        clinic.name = request.POST["name"]
        clinic.feature_image = request.FILES["feature_image"]
        clinic.description = request.POST["description"]
        clinic.department= request.POST["department"]
        #clinic.established_at = request.POST["established_at"]

        if "feature_image" in request.FILES:
            clinic.feature_image = request.FILES["feature_image"]
        clinic.save()

        return redirect("main_app:clinic_detail", clinic_id=clinic.id)

    return render(request, 'main_app/update_clinic.html', {"clinic" : clinic, "iso_date" : iso_date, "appointments" : appointments})

def delete_clinic (request:HttpRequest,clinic_id):
    clinic = Clinic.objects.get(id=clinic_id)
    clinic.delete()

    return redirect("main_app:homePage")


def book_appointment(request:HttpRequest, clinic_id):
    if request.method == "POST":
        clinic_object = Clinic.objects.get(id=clinic_id)
        #addin a new appointment in database
        new_appoinment = Appointment(user=request.user,
                            clinic=clinic_object,
                            case_description=request.POST["case_description"],
                            patient_age=request.POST["patient_age"],
                            appointment_datetime=request.POST["appointment_datetime"])
        
        new_appoinment.save()

        '''appointment_datetime=request.POST["appointment_datetime"]

        appointment = Appointment.objects.filter(appointment_datetime = appointment_datetime)'''

         # Check if appointment is booked

        '''if appointment.exists():
            msg = "Please choose another datetime!"
            age = range(1, 100)
            clinic = Clinic.objects.get(id = clinic_id)
            appointment = Appointment.objects.filter(clinic = clinic, user = request.user)
            return render(request, 'main_app/clinics_detail.html', {'clinic': clinic, 'appointment': appointment, 'msg': msg})
        
        else:
            new_appointment = Appointment(
                clinic = clinic_object,
                user = request.user,
                case_description = request.POST["case_description"],
                patient_age = request.POST["patient_age"],
                appointment_datetime = request.POST["appointment_datetime"]
            )
            new_appointment.save()'''


    return redirect("main_app:clinic_detail", clinic_id=clinic_id)


def searchPage(request:HttpRequest):
    search_phrase = request.GET.get("search", "")
    clinics = Clinic.objects.filter(name__contains=search_phrase)

    return render(request, "main_app/search.html", {"clinics" : clinics})


    







