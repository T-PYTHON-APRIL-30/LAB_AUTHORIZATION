from django.contrib import admin
from .models import Clinic,Appointment

# Register your models here.
class ClinicAdmin(admin.ModelAdmin):
    list_display = ('name','description','department')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user','patient_age','clinic', 'appointment_datetime', 'is_attended')
    list_filter = ('appointment_datetime',)



admin.site.register(Clinic,ClinicAdmin)
admin.site.register(Appointment,AppointmentAdmin)