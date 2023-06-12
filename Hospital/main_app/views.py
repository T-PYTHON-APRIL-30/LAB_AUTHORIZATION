from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Clinic, Appointment,User

# Create your views here.
def home(request: HttpRequest):
    clinic = Clinic.objects.all()

    return render(request, 'main_app/home.html', {'clinic': clinic})


def clinics(request: HttpRequest):
    clinic = Clinic.objects.all()

    return render(request, 'main_app/clinics.html', {'clinic': clinic})


def search(request: HttpRequest):
    search_phrase = request.GET.get("search", "")
    clinic = Clinic.objects.filter(name__icontains = search_phrase) or Clinic.objects.filter(department__icontains = search_phrase)

    return render(request, 'main_app/search.html', {"clinic" : clinic})


def clinics_detail(request: HttpRequest, clinic_id):
    age = range(1, 100)
    clinic = Clinic.objects.get(id = clinic_id)
    appointment = Appointment.objects.filter(clinic = clinic, user = request.user )

    return render(request, 'main_app/clinic_detail.html', {'clinic': clinic, 'age': age, 'appointment': appointment})


def booking(request: HttpRequest, clinic_id):
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

    return redirect('main_app:clinics_detail', clinic_id = clinic_id)


def manager(request: HttpRequest):
    if not request.user.is_staff:
        return redirect("users_app:no_permission")

    return render(request, 'main_app/manager.html')


def manager_add(request: HttpRequest):
    clinic = Clinic.objects.all()

    if not request.user.is_staff:
        return redirect("users_app:no_permission")

    if request.method == "POST":
        new_clinic = Clinic(
            name = request.POST["name"], 
            description = request.POST["description"], 
            department = request.POST["department"], 
            feature_image = request.FILES["feature_image"]
        )
        new_clinic.save()
        return redirect("main_app:clinics")

    return render(request, 'main_app/manager_add.html', {'clinic': clinic})


def manager_update(request: HttpRequest, clinic_id):
    clinics = Clinic.objects.all()
    clinic = Clinic.objects.get(id = clinic_id)

    if not request.user.is_staff:
        return redirect("users_app:no_permission")

    if request.method == "POST":
        clinic.name = request.POST["name"]
        clinic.description = request.POST["description"]
        clinic.department = request.POST["department"]

        if "image" in request.FILES:
            clinic.feature_image = request.FILES["feature_image"]
        clinic.save()

        return redirect("main_app:clinics_detail", clinic_id = clinic_id)

    return render(request, 'main_app/manager_update.html', {'clinic': clinic, 'clinics': clinics})


def manager_appointments(request: HttpRequest):
        if not (request.user.is_staff):
            return redirect("users_app:no_permission")

        appointment = Appointment.objects.all()

        return render(request, 'main_app/appointments.html', {'appointment': appointment})


def appointments_add(request: HttpRequest):
    if not (request.user.is_staff and request.user.has_perm("main_app.add_appointment")):
        return redirect("users_app:no_permission")

    age = range(1, 100)
    user = User.objects.all()
    clinic = Clinic.objects.all()

    if request.method == "POST":
        date = request.POST["date"]
        time = request.POST["time"]
        clinic_object = Clinic.objects.get(id = request.POST["clinic"])
        user_object = User.objects.get(id = request.POST["user"])
        new_appointment = Appointment(
            clinic = clinic_object,
            user = user_object,
            case_description = request.POST["case_description"],
            patient_age = request.POST["patient_age"],
            appointment_datetime = date + " " + time
        )
        new_appointment.save()

        return redirect('main_app:manager_appointments')

    return render(request, 'main_app/appointments_add.html', {'age': age, 'user': user, 'clinic': clinic})


def appointments_delete(request: HttpRequest, appointment_id):
    if not (request.user.is_staff and request.user.has_perm("main_app.delete_appointment")):
        return redirect("users_app:no_permission")

    appointment = Appointment.objects.get(id = appointment_id)
    appointment.delete()

    return redirect('main_app:manager_appointments')


def appointments_update(request: HttpRequest, appointment_id):
    if not (request.user.is_staff and request.user.has_perm("main_app.change_appointment")):
        return redirect("users_app:no_permission")

    appointment = Appointment.objects.get(id = appointment_id)
  
    if request.method == "POST":
        date = request.POST["date"]
        time = request.POST["time"]
        appointment.case_description = request.POST["case_description"]
        appointment.appointment_datetime = date + " " + time
        appointment.is_attended = request.POST["is_attended"]

        appointment.save()

        return redirect("main_app:manager_appointments")

    return render(request, 'main_app/appointments_update.html', {'appointment': appointment})