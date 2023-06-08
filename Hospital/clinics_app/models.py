from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Clinic(models.Model):
    
    clinic_name = models.CharField(max_length=2084)
    feature_image = models.ImageField(upload_to="images/")
    description = models.TextField()
    department = models.TextChoices("Department",["Heart Center", "Neuroscience Center", "Obesity Center", "Eye Center", "Orthopedic Center", "Pediatric Center"])
    established_at = models.DateField()

class Appointment(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    case_description = models.TextField()
    patient_age = models.IntegerField()
    appointment_datetime = models.DateTimeField(auto_now=True)
    is_attended = models.BooleanField(default=False)