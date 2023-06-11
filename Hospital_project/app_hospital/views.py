from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Clinic, Appointment
# Create your views here.


def home_page(request: HttpRequest):
    clinics = Clinic.objects.all()

    return render(request, "app_hospital/index.html", {"clinics": clinics})


def clinics_detials(request: HttpRequest):

    clinics = Clinic.objects.all()
    return render(request, "app_hospital/clinc_detial.html", {"clinics": clinics})


def clinic_detials(request: HttpRequest, clinic_id):

    clinics = Clinic.objects.get(id=clinic_id)
    return render(request, "app_hospital/clinic_page.html", {"clinics": clinics})


def search_page(request: HttpRequest):

    search_letter = request.GET.get("search", "")
    clinics = Clinic.objects.filter(name__contains=search_letter)

    return render(request, "app_hospital/search.html", {"clinic": clinics})


def add_clinic(request: HttpRequest):

    # if not request.user.is_staff:
    #     return redirect("accounts:no_permission_page")

    if request.method == "POST":
        # addin a new game in database
        new_clinic = Clinic(name=request.POST["name"], feature_image=request.FILES["feature_image"], description=request.POST["description"], department=request.POST["department"],
                            established_at=request.POST["established_at"])
        new_clinic.save()
        return redirect("app_hospital:add_clinic")

    return render(request, "app_hospital/manager.html")


def update_clinic(request: HttpRequest, clinic_id):

    clinics = Clinic.objects.get(id=clinic_id)
    iso = clinics.established_at.isoformat()

    if request.method == "POST":
        clinics.name = request.POST["name"]
        clinics.description = request.POST["description"]
        clinics.department = request.POST["department"]
        clinics.established_at = request.POST["established_at"]

        if "feature_image" in request.FILES:
            clinics.feature_image = request.FILES["feature_image"]
        clinics.save()

        return redirect("app_hospital:one_clinic_detials", clinic_id=clinics.id)
    return render(request, "app_hospital/update.html", {"clinics": clinics, "iso": iso})


def add_appointment(request: HttpRequest, clinic_id):
    if request.method == "POST":
        clinic_object = Clinic.objects.get(id=clinic_id)
        new_appointment = Appointment(
            clinic=clinic_object, user=request.user, case_description=request.POST[
                "case_description"], patient_age=request.POST["patient_age"], appointment_datetime=request.POST["appointment_datetime"]
        )
        new_appointment.save()
    return redirect("app_hospital:add_appointment", clinic_id=clinic_id)
