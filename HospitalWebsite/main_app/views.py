from django.shortcuts import render ,redirect
from django.http import HttpRequest, HttpResponse 
from .models import Clinic, Appointment
# Create your views here.

def index_page(request: HttpRequest):

    clinics = Clinic.objects.all()[:3]

    return render(request, "main_app/index.html", {"clinics":clinics})

def add_update_clinic(request:HttpRequest):
    if not (request.user.is_staff and request.user.has_perm("main_app.add_update_clinic")):
        return redirect("users_app:no_permission_page")
    

    if request.method == "POST":

        new_clinic = Clinic(name=request.POST["name"], feature_image=request.FILES["feature_image"],
                         description=request.POST["description"],department = request.POST["department"], established_at=request.POST["established_at"])
        new_clinic.save()
        return redirect("main_app:index_page")

    return render(request, "main_app/add_update_clinic.html")

def detail(request:HttpRequest, clinic_id):

    try:
        clinic = Clinic.objects.get(id=clinic_id)
    except:
        return render(request, 'main_app/not_found.html')

    return render(request, 'main_app/detail.html', {"clinic" : clinic})

def search(request:HttpRequest):
    search_phrase = request.GET.get("search", "")
    clinics = Clinic.objects.filter(name__contains=search_phrase)

    return render(request, "main_app/search.html", {"clinics" : clinics})

def update_clinic(request:HttpRequest, clinic_id):

    clinic = Clinic.objects.get(id=clinic_id)
    iso_date = clinic.established_at.isoformat()
    if request.method == "POST":
        clinic.name = request.POST["name"]
        clinic.description = request.POST["description"]
        clinic.established_at = request.POST["established_at"]

        if "feature_image" in request.FILES:
            clinic.feature_image = request.FILES["feature_image"]
        clinic.save()

        return redirect("main_app:detail", clinic_id=clinic.id)

    return render(request, 'main_app/update_clinic.html', {"clinic" : clinic, "iso_date" : iso_date})

def book_appointment(request:HttpRequest, clinic_id):

    if request.method == "POST":
        clinic_object = Clinic.objects.get(id=clinic_id)
        new_appointment = Appointment(clinic=clinic_object, user=request.user, case_description=request.POST["case_description"], patient_age=request.POST["patient_age"],
                                      appointment_datetime=request.POST["appointment_datetime"])
        new_appointment.save()

    return redirect("main_app:detail", clinic_id=clinic_id)





