from django.contrib import admin
from .models import Clinic, Appointment

# Register your models here.

class ClinicAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'department')

admin.site.register(Clinic, ClinicAdmin)
admin.site.register(Appointment)