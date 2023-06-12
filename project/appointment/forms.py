from django import forms
from appointment.models import Appointment


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ("name" ,"discription","patient_age","phone_number" ,"appointment_datetime",)
        
        

