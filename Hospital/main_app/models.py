from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Clinic(models.Model):
    CHOICES = (
        ('Heart Center', 'Heart Center'),
        ('Neuroscience Center', 'Neuroscience Center'),
        ('Obesity Center', 'Obesity Center'),
        ('Eye Center', 'Eye Center'),
        ('Orthopedic Center', 'Orthopedic Center'),
        ('Pediatric Center', 'Pediatric Center')
    )

    name = models.CharField(max_length = 100)
    feature_image = models.ImageField(upload_to = 'img/')
    description = models.TextField()
    department = models.CharField(max_length = 100, choices = CHOICES)
    established_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.name}"


class Appointment(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    case_description = models.TextField()
    patient_age = models.IntegerField()
    appointment_datetime = models.DateTimeField()
    is_attended = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.user.username} on {self.clinic}"
