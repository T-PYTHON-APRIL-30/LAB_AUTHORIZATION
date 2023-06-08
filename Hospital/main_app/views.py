from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home_page(request: HttpRequest):
    return render(request, 'main_app/home.html')


def clinics_page(request: HttpRequest):
    return render(request, 'main_app/clinics.html')


def clinics_page_detail(request: HttpRequest, clinic_id):
    return render(request, 'main_app/clinics_detail.html')


def booking_page(request: HttpRequest, clinic_id):
    return render(request, 'main_app/booking.html')


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
