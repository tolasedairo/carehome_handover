from django.contrib import admin
from .models import CustomUser, Resident, Handover, EmergencyContact, CarePlanSection

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Resident)
admin.site.register(Handover)
admin.site.register(EmergencyContact)
admin.site.register(CarePlanSection)
