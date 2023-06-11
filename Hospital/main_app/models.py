from django.db import models
from django.contrib.auth.models import User

# Create your models here.

DEP_CHOICES = (
    ('HC', 'Heart Center'),
    ('EUC', 'euroscience Center'),
    ('OBC', 'Obesity Center'),
    ('EYEC', 'Eye Center'),
    ('ORC', 'Orthopedic Center'),
    ('PEC', 'Pediatric Center'),
)

class Clinic(models.Model):
    name = models.CharField(max_length=200)
    feature_image = models.ImageField(upload_to="images/", default="images/default.jpg")
    description = models.TextField()
    department = models.CharField(max_length =100, choices = DEP_CHOICES)
    established_at = models.DateField(auto_now_add=True)
    def __str__(self) -> str:
        return f"{self.name}"

    

class Appointment(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    case_description = models.TextField()
    patient_age = models.IntegerField()
    appointment_datetime = models.DateTimeField()
    is_attended = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}"

