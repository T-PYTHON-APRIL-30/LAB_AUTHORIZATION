from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Clinic,Appointment

# Create your views here.

def index_page(request:HttpRequest):

    if request.user.is_authenticated:
        print(request.user.first_name)

    clinics = Clinic.objects.all()

    return render(request, "main_app/index.html", {"clinics" : clinics})



def add_clinic(request:HttpRequest):

    if not request.user.is_staff:
        return redirect("accounts:no_permission_page")

    if request.method == "POST":
        #addin a new clinic in database
        new_clinic = Clinic(name=request.POST["name"], description=request.POST["description"], department=request.POST["department"], feature_image=request.FILES["feature_image"])
        new_clinic.save()
        return redirect("main_app:index_page")

    return render(request, "main_app/add_clinic.html")



def update_clinic(request:HttpRequest, clinic_id):
    if not (request.user.has_perm("main_app.change_clinic")):
        return redirect("accounts:no_permission_page")
    
    clinic = Clinic.objects.get(id=clinic_id)

    #updating the clinic
    if request.method == "POST":
        clinic.name = request.POST["name"]
        clinic.description = request.POST["description"]
        clinic.department = request.POST["department"]
        clinic.established_at = request.POST["established_at"]

        if "feature_image" in request.FILES:
            clinic.feature_image = request.FILES["feature_image"]
        clinic.save()

        return redirect("main_app:clinic_detail", clinic_id=clinic.id)

    return render(request, 'main_app/update_clinic.html', {"clinic" : clinic})



def delete_clinic(request:HttpRequest, clinic_id):

    #check that user is staff and has a permission to delete
    if not (request.user.is_staff and  request.user.has_perm("main_app.delete_clinic")):
        return redirect("accounts:no_permission_page")
    
    clinic = Clinic.objects.get(id=clinic_id)
    clinic.delete()

    return redirect("main_app:index_page")



def clinic_detail(request:HttpRequest, clinic_id):

    try:
        clinic = Clinic.objects.get(id=clinic_id)
    except:
        return render(request, 'main_app/not_found.html')

    return render(request, 'main_app/clinic_detail.html', {"clinic" : clinic})


def make_appointment(request:HttpRequest, clinic_id):

    if request.method == "POST":
        clinic_object = Clinic.objects.get(id=clinic_id)
        new_appointment = Appointment(clinic=clinic_object, user=request.user, case_description=request.POST["case_description"], patient_age=request.POST["patient_age"],appointment_datetime=request.POST["appointment_datetime"])
        new_appointment.save()
    
    return redirect("main_app:clinic_detail", clinic_id=clinic_id)



def appointment_view(request:HttpRequest):

    if not (request.user.is_staff and  request.user.has_perm("main_app.add_appointment")):
        appointment_user=Appointment.objects.filter(user=request.user)
    else:
        appointment_user=Appointment.objects.all()
    return render(request,"main_app/appointment_view.html",{"appointment_user":appointment_user })


def search_page(request:HttpRequest):
    search_phrase = request.GET.get("search", "")
    clinics = Clinic.objects.filter(name__contains=search_phrase)

    return render(request, "main_app/search_page.html", {"clinics" : clinics})





    