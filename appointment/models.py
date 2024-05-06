from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User  

class Appointment(models.Model):
    pet_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey('pets.Pet', on_delete=models.CASCADE)  # Assuming you'll have a Pet model
    appointment_datetime = models.DateTimeField()
    
    SERVICE_CHOICES = [
        ('VAC', 'Vaccination'),
        ('CHK', 'Checkup'),
        ('SUR', 'Surgery'),
        ('OTH', 'Other') 
    ]
    service_type = models.CharField(max_length=3, choices=SERVICE_CHOICES)

    STATUS_CHOICES = [
        ('PEN', 'Pending'),
        ('CON', 'Confirmed'),
        ('CAN', 'Cancelled')
    ]
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='PEN')

    reason_for_visit = models.TextField(blank=True)

    class Meta:
        app_label = 'appointment' 
