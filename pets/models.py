from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
