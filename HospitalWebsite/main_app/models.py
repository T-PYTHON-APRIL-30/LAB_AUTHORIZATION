from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime
# Create your models here.

class Clinic(models.Model):
    name = models.CharField(max_length=500)
    feature_image = models.ImageField(upload_to="images/", default="images/footerr1.jpg")
    description = models.TextField()
    DEPARTMENT_CHOICES = [
        ('Heart Center', 'Heart Center'),
        ('Neuroscience Center', 'Neuroscience Center'),
        ('Obesity Center', 'Obesity Center'),
        ('Eye Center', 'Eye Center'),
        ('Orthopedic Center', 'Orthopedic Center'),
        ('Pediatric Center', 'Pediatric Center')
    ]
    established_at = models.DateField()
    department = models.CharField(max_length=255, choices=DEPARTMENT_CHOICES)

    def __str__(self):
        return self.name
    

    def is_available(self, appointment_datetime):
        # Clinic is available on weekdays from 9am to 5pm
        return (
            appointment_datetime.weekday() < 5  # Weekdays only disallow appointments on weekends (Saturday and Sunday)
            and appointment_datetime.time() >= datetime.time(hour=9)  # After 9am
            and appointment_datetime.time() <= datetime.time(hour=17)  # Before 5pm
        )
    
    def get_available_times(self):
        # Generate a list of available timeslots at 30 minute intervals
        now = timezone.now()
        start_time = now.replace(hour=9, minute=0, second=0, microsecond=0)
        end_time = now.replace(hour=17, minute=0, second=0, microsecond=0)
        available_times = []
        while start_time < end_time:
            if self.is_available(start_time):
                available_times.append(start_time.time())
            start_time += datetime.timedelta(minutes=30)
        return available_times    
    

class Appointment(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    case_description = models.TextField()
    patient_age = models.IntegerField()
    appointment_datetime = models.DateTimeField()
    is_attended = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.clinic} - {self.user.username}"
    
    def clean_appointment_datetime(self):
        """Ensure appointment datetime is in the future."""
        if self.appointment_datetime < timezone.now():
            raise ValidationError('Appointment datetime must be in the future.')
        
    def clean(self):
        """Ensure clinic is free on appointment date and time."""
        existing_appointments = Appointment.objects.filter(clinic=self.clinic,appointment_datetime=self.appointment_datetime).exclude(id=self.id)
        if existing_appointments.exists():
            raise ValidationError('Clinic is not available at the specified time.')