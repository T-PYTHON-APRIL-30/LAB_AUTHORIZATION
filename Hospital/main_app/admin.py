from django.contrib import admin
from .models import Clinic, Appointment

# Register your models here.

class ClinicAdmin(admin.ModelAdmin):
    list_display = ('name', 'feature_image', 'description', 'department')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'clinic', 'case_description','patient_age','appointment_datetime','is_attended')
    list_filter = ('clinic',)

admin.site.register(Clinic)
admin.site.register(Appointment)

