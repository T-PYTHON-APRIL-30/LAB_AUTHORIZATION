from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Clinic, Appointment
from django.contrib.auth.models import User

# Create your views here.
def home_page(request: HttpRequest):
    clinic = Clinic.objects.all()[:3]

    return render(request, 'main_app/home.html', {'clinic': clinic})


def clinics_page(request: HttpRequest):
    clinic = Clinic.objects.all()

    return render(request, 'main_app/clinics.html', {'clinic': clinic})


def search_page(request: HttpRequest):
    search_phrase = request.GET.get("search", "")
    clinic = Clinic.objects.filter(name__contains = search_phrase) | Clinic.objects.filter(department__contains = search_phrase)

    return render(request, 'main_app/search.html', {"clinic" : clinic})


def clinics_page_detail(request: HttpRequest, clinic_id):
    age = range(1, 100)
    clinic = Clinic.objects.get(id = clinic_id)
    appointment = Appointment.objects.filter(clinic = clinic, user = request.user)

    return render(request, 'main_app/clinics_detail.html', {'clinic': clinic, 'age': age, 'appointment': appointment})


def booking_page(request: HttpRequest, clinic_id):
    if request.method == "POST":
        clinic_object = Clinic.objects.get(id = clinic_id)
        new_appointment = Appointment(
            clinic = clinic_object,
            user = request.user,
            case_description = request.POST["case_description"],
            patient_age = request.POST["patient_age"],
            appointment_datetime = request.POST["appointment_datetime"]
        )
        new_appointment.save()

    return redirect('main_app:clinics_page_detail', clinic_id = clinic_id)


def manager_page(request: HttpRequest):
    if not (request.user.is_staff):
        return redirect("users_app:no_permission_page")

    return render(request, 'main_app/manager.html')


def manager_page_add(request: HttpRequest):
    if not (request.user.is_staff and request.user.has_perm("main_app.add_clinic")):
        return redirect("users_app:no_permission_page")

    clinic = Clinic.objects.all()
    
    if request.method == "POST":
        new_clinic = Clinic(
            name = request.POST["name"], 
            description = request.POST["description"], 
            department = request.POST["department"], 
            feature_image = request.FILES["feature_image"]
        )
        new_clinic.save()
        return redirect("main_app:clinics_page")

    return render(request, 'main_app/manager_add.html', {'clinic': clinic})


def manager_page_update(request: HttpRequest, clinic_id):
    if not (request.user.is_staff and request.user.has_perm("main_app.change_clinic")):
        return redirect("users_app:no_permission_page")
    
    clinics = Clinic.objects.all()
    clinic = Clinic.objects.get(id = clinic_id)

    if request.method == "POST":
        clinic.name = request.POST["name"]
        clinic.description = request.POST["description"]
        clinic.department = request.POST["department"]
        
        if "image" in request.FILES:
            clinic.feature_image = request.FILES["feature_image"]
        clinic.save()

        return redirect("main_app:clinics_page_detail", clinic_id = clinic.id)

    return render(request, 'main_app/manager_update.html', {'clinic': clinic, 'clinics': clinics})


def manager_page_appointments(request: HttpRequest):
    if not (request.user.is_staff):
        return redirect("users_app:no_permission_page")

    appointment = Appointment.objects.all()

    return render(request, 'main_app/appointments.html', {'appointment': appointment})


def appointments_page_add(request: HttpRequest):
    if not (request.user.is_staff and request.user.has_perm("main_app.add_appointment")):
        return redirect("users_app:no_permission_page")
    
    age = range(1, 100)
    user = User.objects.all()
    clinic = Clinic.objects.all()

    if request.method == "POST":
        clinic_object = Clinic.objects.get(id = request.POST["clinic"])
        user_object = User.objects.get(id = request.POST["user"])
        new_appointment = Appointment(
            clinic = clinic_object,
            user = user_object,
            case_description = request.POST["case_description"],
            patient_age = request.POST["patient_age"],
            appointment_datetime = request.POST["appointment_datetime"]
        )
        new_appointment.save()
        
        return redirect('main_app:manager_page_appointments')

    return render(request, 'main_app/appointments_add.html', {'age': age, 'user': user, 'clinic': clinic})


def appointments_page_delete(request: HttpRequest, appointment_id):
    if not (request.user.is_staff and request.user.has_perm("main_app.delete_appointment")):
        return redirect("users_app:no_permission_page")
    
    appointment = Appointment.objects.get(id = appointment_id)
    appointment.delete()

    return redirect('main_app:manager_page_appointments')


def appointments_page_update(request: HttpRequest, appointment_id):
    if not (request.user.is_staff and request.user.has_perm("main_app.change_appointment")):
        return redirect("users_app:no_permission_page")

    appointment = Appointment.objects.get(id = appointment_id)
    iso_date = appointment.appointment_datetime.isoformat()

    if request.method == "POST":
        appointment.case_description = request.POST["case_description"]
        appointment.appointment_datetime = request.POST["appointment_datetime"]
        appointment.is_attended = request.POST["is_attended"]
        
        appointment.save()

        return redirect("main_app:manager_page_appointments")

    return render(request, 'main_app/appointments_update.html', {'appointment': appointment, 'iso_date': iso_date})
