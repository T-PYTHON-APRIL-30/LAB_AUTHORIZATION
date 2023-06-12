from django.contrib import admin
from .models import Clinic, Appointment

# Register your models here.
class ClinicAdmin(admin.ModelAdmin):
    list_display = ('name', 'department',)


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'clinic',)


admin.site.register(Clinic, ClinicAdmin)
admin.site.register(Appointment, AppointmentAdmin)