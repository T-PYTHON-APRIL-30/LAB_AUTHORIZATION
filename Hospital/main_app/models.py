from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.

class Clinic (models.Model):
    name = models.CharField(max_length=1000)
    feature_image = models.ImageField(upload_to="images/", default="images/default.jpg")
    description = models.TextField() 
    departments_type = models.TextChoices("Clinic Department", ["Heart Center","Neuroscience Center","Obesity Center","Eye Center","Orthopedic Center","Pediatric Center"])
    department = models.CharField(max_length=300, choices=departments_type.choices)
    established_at = models.DateField(default=datetime.date.today)


    def __str__(self) -> str:
        return f"{self.name}"

class Appointment (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    case_description = models.TextField()
    patient_age = models.CharField(max_length=100)
    appointment_datetime = models.DateTimeField()
    is_attended = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.user.username} on {self.clinic}"



