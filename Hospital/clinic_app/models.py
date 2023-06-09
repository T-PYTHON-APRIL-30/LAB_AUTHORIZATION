from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Clinic(models.Model):
    name = models.CharField(max_length=100)
    feature_image = models.ImageField(upload_to='static/img')
    description = models.TextField()
    DEPARTMENT_CHOICES = [
        ('Heart Center', 'Heart Center'),
        ('Neuroscience Center', 'Neuroscience Center'),
        ('Obesity Center', 'Obesity Center'),
        ('Eye Center', 'Eye Center'),
        ('Orthopedic Center', 'Orthopedic Center'),
        ('Pediatric Center', 'Pediatric Center'),
    ]
    
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    established_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    case_description = models.TextField()
    patient_age = models.PositiveIntegerField()
    appointment_datetime = models.DateField()
    is_attended = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.user.username}'s appointment at {self.clinic.name}"
