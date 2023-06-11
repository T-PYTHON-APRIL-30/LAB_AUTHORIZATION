from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from main_app.models import Clinic


class Appointment(models.Model):
    timeAvailable = [
        ('10.00 Pm', '10.00 Pm'),
        ('10.30 Pm', '10.30 Pm'),
        ('11.00 Pm', '11.00 Pm'),
        ('11.30 Pm', '10.30 Pm'),
        ('12.00 Pm', '12.00 Pm'),
        ('12.30 Pm', '12.30 Pm'),
        ('1.00 Pm', '1.00 Pm'),
        ('1.30 Pm', '1.30 Pm'),
        ('2.00 Pm', '2.00 Pm'),
        ('2.30 Pm', '2.30 Pm'),
        ('3.00 Pm', '3.00 Pm'),
        ('3.30 Pm', '3.30 Pm'),
        ('4.00 Pm', '4.00 Pm'),
        ('4.30 Pm', '4.30 Pm'),
        ('5.00 Pm', '5.00 Pm'),
        ('5.30 Pm', '5.30 Pm'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    patient_age = models.IntegerField()
    discription = models.TextField(max_length=500)
    phone_number = models.CharField(max_length=120)
    appointment_datetime = models.CharField(choices=timeAvailable, max_length=30, unique=True)
    is_attended = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)  


    def __str__(self):
        return self.name



