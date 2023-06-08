from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Clinic, Appointment

# Create your views here.
def home_page(request: HttpRequest):
    clinic = Clinic.objects.all()[:3]

    return render(request, 'main_app/home.html', {'clinic': clinic})


def clinics_page(request: HttpRequest):
    clinic = Clinic.objects.all()[:3]

    return render(request, 'main_app/clinics.html', {'clinic': clinic})


def search_page(request: HttpRequest):
    search_phrase = request.GET.get("search", "")
    clinic = Clinic.objects.filter(name__contains = search_phrase) | Clinic.objects.filter(department__contains = search_phrase)

    return render(request, 'main_app/search.html', {"clinic" : clinic})


def clinics_page_detail(request: HttpRequest, clinic_id):
    age = range(1, 100)
    clinic = Clinic.objects.get(id = clinic_id)
    appointment = Appointment.objects.all()

    return render(request, 'main_app/clinics_detail.html', {'clinic': clinic, 'age': age, 'appointment': appointment})


def booking_page(request: HttpRequest, clinic_id):
    if request.method == "POST":
        new_appointment = Appointment(
            case_description = request.POST["case_description"],
            patient_age = request.POST["patient_age"],
            appointment_datetime = request.POST["appointment_datetime"]
        )
        new_appointment.save()
        return redirect('main_app:clinics_page_detail', clinic_id)

    return render(request, 'main_app/clinics_detail.html')


def manager_page(request: HttpRequest):
    return render(request, 'main_app/manager.html')


def manager_page_add(request: HttpRequest):
    return render(request, 'main_app/manager_add.html')


def manager_page_update(request: HttpRequest, clinic_id):
    return render(request, 'main_app/manager_update.html')


def manager_page_appointments(request: HttpRequest):
    return render(request, 'main_app/appointments.html')


def appointments_page_add(request: HttpRequest):
    return render(request, 'main_app/appointments_add.html')


def appointments_page_delete(request: HttpRequest, clinic_id):
    return redirect('main_app:manager_page_appointments')


def appointments_page_update(request: HttpRequest, clinic_id):
    return render(request, 'main_app/appointments_update.html')
