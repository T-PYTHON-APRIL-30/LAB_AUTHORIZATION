from django.contrib import admin
from .models import Clinic, Appointment

# Register your models here.
class ClinicAdmin(admin.ModelAdmin):
    list_display = ('name', 'feature_image', 'description', 'established_at')


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'clinic', 'case_description')
    list_filter = ('clinic',)

admin.site.register(Clinic, ClinicAdmin)
admin.site.register(Appointment, AppointmentAdmin)
