from django.shortcuts import render
from django.http import HttpResponse
from .decorators import role_based_access
from .models import Resident


# Create your views here.
def home(request):
    return HttpResponse("Welcome to Care Home Handover App")


@role_based_access(['manager', 'senior_carer', 'carer'])
def residents_list(request):
    user_role = request.user.role

    if user_role in ['manager', 'senior_carer']:
        residents = Resident.objects.all()  # Full info
    else:
        # Carers only see limited info
        residents = Resident.objects.all().only('id', 'first_name', 'last_name', 'room_number')

    context = {
        'residents': residents,
        'user_role': user_role
    }
    return render(request, 'carehome/residents_list.html', context)