from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#  "Heart Center", "Neuroscience Center", "Obesity Center", "Eye Center", "Orthopedic Center", "Pediatric Center"



class Clinic(models.Model):
    name = models.CharField(max_length = 150)
    image = models.ImageField(upload_to="images/")
    description=models.TextField()
    

    department_CHOICES=[
    ("Heart Center","Heart Center"),
    ("Neuroscience Center","Neuroscience Center"),
    ("Obesity Center","Obesity Center"),
    ("Eye Center","Eye Center"),
    ("Orthopedic Center","Orthopedic Center"),
    ("Pediatric Center","Pediatric Center")
]
    
    department=models.CharField(max_length=50,choices=department_CHOICES)
    established_at=models.DateField()
    
    def __str__(self) -> str:
        return f"{self.name}"



class Appointment(models.Model):
    clinic=models.ForeignKey(Clinic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    case_description=models.TextField()
    patient_age=models.IntegerField()
    appointment_datetime=models.DateTimeField()
    is_attended =models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.user.username} on {self.clinic}"


  

