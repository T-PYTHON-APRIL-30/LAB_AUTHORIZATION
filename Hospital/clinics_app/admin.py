from django.contrib import admin
from .models import Clinic , Appointment 
# Register your models here.
class ClinicAdmin(admin.ModelAdmin):
    list_display = ('clinic_name','feature_image','description','department','established_at')
    list_filter = ('department','established_at')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user','clinic','case_description','patient_age','appointment_datetime','is_attended')
    list_filter = ('is_attended','appointment_datetime')

admin.site.register(Clinic,ClinicAdmin)
admin.site.register(Appointment,AppointmentAdmin)