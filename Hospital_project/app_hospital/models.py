from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Clinic(models.Model):
    DEPARTMENT_CHOICES = [
        ('heart', 'Heart Center'),
        ('neuro', 'Neuroscience Center'),
        ('obesity', 'Obesity Center'),
        ('eye', 'Eye Center'),
        ('ortho', 'Orthopedic Center'),
        ('pediatric', 'Pediatric Center'),
    ]
    name = models.CharField(max_length=100)
    feature_image = models.ImageField(upload_to='images/')
    description = models.TextField()
    department = models.CharField(max_length=10, choices=DEPARTMENT_CHOICES)
    established_at = models.DateField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    case_description = models.TextField()
    patient_age = models.PositiveIntegerField()
    appointment_datetime = models.DateTimeField()
    is_attended = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.clinic.name}"
