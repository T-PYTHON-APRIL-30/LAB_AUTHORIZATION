from django.db import models
from django.contrib.auth.models import User


# Create your models here.

Heart = "Heart Center"
Neuroscience =  "Neuroscience Center"
Obesity = "Obesity Center"
Eye = "Eye Center"
Orthopedic = "Orthopedic Center"
Pediatric = "Pediatric Center"



class Clinic(models.Model):
    name = models.CharField(max_length=512)
    feature_image = models.ImageField(upload_to="images/", default="images/default.png")
    description = models.TextField()
    DEP_CHOICES = [
           (Heart, "Heart Center"),
           (Neuroscience, "Neuroscience Center"),
           (Obesity, "Obesity Center"),
           (Eye, "Eye Center"),
           (Orthopedic, "Orthopedic Center"),
           (Pediatric, "Pediatric Center"),
    ]
    department = models.CharField(max_length = 20, choices = DEP_CHOICES, default = 'Heart Center')
    established_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name}"

class Appointment(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, null=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    case_description = models.TextField()
    patient_age = models.IntegerField()
    appointment_datetime = models.DateTimeField()
    is_attended = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.clinic.name}"