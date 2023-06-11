from django.contrib import admin
from .models import Clinic, Appointment

# Register your models here.
admin.site.register(Clinic)
admin.site.register(Appointment)