from django.db import models

# Create your models here.
from django.db import models

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

class Counsellor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    counsellor = models.ForeignKey(Counsellor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
