from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Clinic(models.Model):
    department = (
    ('Heart Center', "Heart Center"),
    ('Neuroscience Center', "Neuroscience Center"),
    ('Obesity Center', "Obesity Center"),
    ('Orthopedic Center', 'Orthopedic Center'),
    ('Pediatric Center', 'Pediatric Center'),
    ('Eye Center', 'Eye Center'),
)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    feature_image = models.ImageField()
    discription = models.TextField(max_length=500)
    department = models.CharField(choices=department, max_length=100)
    established_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
