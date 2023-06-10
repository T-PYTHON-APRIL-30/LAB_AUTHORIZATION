from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Clinic(models.Model):
    
    department_choices= (
    ('Neuroscience Center','Neuroscience Center'),
    ('Heart Center','Heart Center'),
    ('Obesity Center','Obesity Center'),
    ('Eye Center','Eye Center'),
    ('Orthopedic Center','Orthopedic Center'),
    ('Pediatric Center','Pediatric Center'),
    )

    clinic_name = models.CharField(max_length=2084)
    feature_image = models.ImageField(upload_to="images/")
    description = models.TextField()
    department = models.CharField(max_length= 50, choices=department_choices)
    established_at = models.DateField()

    def __str__(self) -> str:
        return f"{self.clinic_name}"

class Appointment(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    user = models.OneToOneField(User,on_delete=models.PROTECT)

    case_description = models.TextField()
    patient_age = models.IntegerField()
    appointment_datetime = models.DateTimeField(auto_now=True)
    
    is_attended = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.user.username} on {self.clinic}"