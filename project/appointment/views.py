from .models import *
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm







@login_required
def appointment_list(request):
    if not (request.user.has_perm("appointment.change_appointment") and request.user.has_perm("appointment.delete_appointment")):
        return redirect("main_app:home")

    appointment_list  = Appointment.objects.all()


    if 'appointmenupdate' in request.POST :
        if request.user.is_authenticated:
            appointmentId = request.POST.get('appointmentId')

            appointmenItem= Appointment.objects.get(id=appointmentId)
            appointmenItem.is_attended = True
            appointmenItem.save()

            
    if 'appointmendelete' in request.POST :
        if request.user.is_authenticated:
            appointmentId = request.POST.get('appointmentId')

            appointmenItem= Appointment.objects.get(id=appointmentId)
            appointmenItem.delete()


    return render(request ,'appointment_list.html', {
        'appointment_list' : appointment_list ,

    })
    
@login_required 
def appointment_list_category(request , department): 
    department_name =department

    appointments = Appointment.objects.filter(clinic__department=department_name)


    if 'appointmenupdate' in request.POST :
        if request.user.is_authenticated:
            appointmentId = request.POST.get('appointmentId')

            appointmenItem= Appointment.objects.get(id=appointmentId)
            appointmenItem.is_attended = True
            appointmenItem.save()

            
    if 'appointmendelete' in request.POST :
        if request.user.is_authenticated:
            appointmentId = request.POST.get('appointmentId')

            appointmenItem= Appointment.objects.get(id=appointmentId)
            appointmenItem.delete()
    return render(request ,'appointment_list_category.html', {
        'appointments' : appointments ,

    })




@login_required 
def appointment_detail(request , id):
    appointment_detail  = get_object_or_404(Appointment, id=id)

    return render(request ,'appointment_detail.html', {
        'appointment_detail' : appointment_detail ,

    })
    
@login_required 
def add_Appointment(request, id=id):
    clinic = Clinic.objects.get(id=id)

    if request.method == 'POST':
        appointment_form = AppointmentForm(request.POST)
        if appointment_form.is_valid():
            appointment = appointment_form.save(commit=False)
            appointment.clinic = clinic
            appointment.user = request.user

            existing_appointment = Appointment.objects.filter(
                clinic=clinic,
                appointment_datetime=appointment.appointment_datetime
            ).first()

            if existing_appointment:
                error_message = "This appointment datetime is already booked. Please choose a different one."
                return render(request, 'add_appointment.html', {'appointment_form': appointment_form, 'error_message': error_message})

            appointment.save()
            return redirect('main_app:home')

    else:
        appointment_form = AppointmentForm()

    return render(request, 'add_appointment.html', {'appointment_form': appointment_form})

    

    
    
@login_required
def appointment_delete(request , pk):
    appointment_delete = Appointment.objects.get(pk=pk)
    appointment_delete.delete()
    return redirect('main_app:home')



