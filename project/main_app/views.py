from .models import *
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required
from .forms import ClinicForm



@login_required
def home(request):
    clinic_list  = Clinic.objects.all()


    return render(request ,'home.html', {
        'clinic_list' : clinic_list ,

    })


@login_required
def clinic_list(request):
    clinic_list  = Clinic.objects.all()

    return render(request ,'my_clinic_list.html', {
        'clinic_list' : clinic_list ,

    })
    
@login_required 
def clinic_detail(request , id):
    clinic_detail  = get_object_or_404(Clinic, id=id)

    return render(request ,'clinic_detail.html', {
        'clinic_detail' : clinic_detail ,

    })
    
@login_required 
def add_clinic(request):
    clinic_form = ClinicForm(request.POST or None , request.FILES)
    if request.method == 'POST':
        clinic_form = ClinicForm(request.POST or None , request.FILES)
        if clinic_form.is_valid():
            check_user_request = clinic_form.save(commit=False)
            check_user_request.user = request.user
            check_user_request.save()
            return redirect('main_app:home')

    else:
        clinic_form = ClinicForm()
    return render(request ,'add_clinic.html', {
        'clinic_form' : clinic_form ,
    })
    

    
    
@login_required
def clinic_delete(request , pk):
    clinic_delete = Clinic.objects.get(pk=pk)
    clinic_delete.delete()


def search_page(request:HttpRequest):
    
    search_phrase = request.GET.get("query", "")
    clinics = Clinic.objects.filter(department__contains=search_phrase)

    return render(request, "search_page.html", {"clinics" : clinics})