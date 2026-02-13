from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('manager', 'Manager'),
        ('senior_carer', 'Senior Carer'),
        ('carer', 'Carer'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.role})"


class Resident(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    room_number = models.CharField(max_length=10)

    medical_notes = models.TextField(blank=True)
    allergies = models.TextField(blank=True)
    care_plan = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Room {self.room_number})"


class Handover(models.Model):
    SHIFT_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('night', 'Night'),
    ]

    resident = models.ForeignKey(
        Resident, on_delete=models.CASCADE, related_name='handovers'
    )
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    shift = models.CharField(max_length=20, choices=SHIFT_CHOICES)
    notes = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Handover for {self.resident} - {self.shift}"
