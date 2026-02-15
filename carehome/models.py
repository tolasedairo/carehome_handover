from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


# ==============================
# Custom User
# ==============================

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('manager', 'Manager'),
        ('senior_carer', 'Senior Carer'),
        ('carer', 'Carer'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.role})"


# ==============================
# Resident
# ==============================

class Resident(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    preferred_name = models.CharField(max_length=100, blank=True)
    room_number = models.CharField(max_length=10)

    date_of_birth = models.DateField(null=True, blank=True)
    date_of_admission = models.DateField(null=True, blank=True)

    allergies = models.TextField(blank=True)
    photo = models.ImageField(upload_to='residents/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# ==============================
# Emergency Contact
# ==============================

class EmergencyContact(models.Model):
    resident = models.ForeignKey(
        Resident,
        on_delete=models.CASCADE,
        related_name="contacts"
    )

    name = models.CharField(max_length=200)
    relationship = models.CharField(max_length=100)

    home_phone = models.CharField(max_length=20, blank=True)
    work_phone = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=20, blank=True)

    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.resident})"


# ==============================
# Care Plan Section
# ==============================

class CarePlanSection(models.Model):

    SECTION_CHOICES = [
        ("understanding", "Level of Understanding"),
        ("communication", "Communication"),
        ("mobility", "Mobility"),
        ("personal_care", "Personal Care"),
        ("continence", "Continence Care"),
        ("oral_care", "Oral Care"),
        ("nutrition", "Nutrition and Hydration"),
        ("skin_care", "Skin Care"),
        ("social", "Social Interests and Activities"),
        ("night_support", "Night Time Support"),
        ("emotional", "Emotional Support"),
        ("sexuality", "Expressing Sexuality"),
        ("spiritual", "Spiritual and Cultural Wellbeing"),
        ("health", "Health Care"),
        ("medication", "Medication Management"),
        ("mental", "Mental Health"),
        ("end_of_life", "End of Life Preferences"),
        ("breathing", "Breathing"),
    ]

    resident = models.ForeignKey(
        Resident,
        on_delete=models.CASCADE,
        related_name="care_sections"
    )

    section_type = models.CharField(
        max_length=50,
        choices=SECTION_CHOICES
    )

    current_needs = models.TextField()
    desired_outcomes = models.TextField()
    staff_support = models.TextField()

    date_started = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    ongoing = models.BooleanField(default=True)

    last_modified = models.DateTimeField(auto_now=True)

    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    resident_signature = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.resident} - {self.get_section_type_display()}"


# ==============================
# Handover
# ==============================

class Handover(models.Model):
    SHIFT_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('night', 'Night'),
    ]

    resident = models.ForeignKey(
        Resident,
        on_delete=models.CASCADE,
        related_name='handovers'
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    shift = models.CharField(max_length=20, choices=SHIFT_CHOICES)
    notes = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Handover for {self.resident} - {self.shift}"
