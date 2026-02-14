from django.shortcuts import render
from django.http import HttpResponse
from .decorators import role_based_access
from .models import Resident
from .models import Handover
from django.contrib.auth.decorators import login_required
from .forms import HandoverForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


# Create your views here.
def home(request):
    return render(request, "carehome/home.html")

@role_based_access(['manager', 'senior_carer', 'carer'])
def residents_list(request):
    user_role = request.user.role

    if user_role in ['manager', 'senior_carer']:
        residents = Resident.objects.all()  # Full info
    else:
        # Carers only see limited info
        residents = Resident.objects.all().only(
            'id', 'first_name', 'last_name', 'room_number'
        )

    context = {
        'residents': residents,
        'user_role': user_role
    }
    return render(request, 'carehome/residents_list.html', context)


@login_required
@role_based_access(['manager', 'senior_carer', 'carer'])
def handover_list(request):

    if request.user.role in ['manager', 'senior_carer']:
        handovers = Handover.objects.all().order_by('-created_at')
    else:
        # carers see limited info
        handovers = Handover.objects.all().only(
            'resident',
            'shift',
            'notes',
            'created_at'
        ).order_by('-created_at')

    return render(request, 'carehome/handover_list.html', {
        'handovers': handovers
    })


@login_required
@role_based_access(['manager', 'senior_carer', 'carer'])
def create_handover(request, resident_id):
    resident = get_object_or_404(Resident, id=resident_id)

    if request.method == 'POST':
        form = HandoverForm(request.POST)
        if form.is_valid():
            handover = form.save(commit=False)
            handover.resident = resident  # <-- Link to resident
            handover.created_by = request.user
            handover.save()
            return redirect('resident_handovers', resident_id=resident.id)
    else:
        form = HandoverForm()

    return render(request, 'carehome/create_handover.html', {
        'form': form,
        'resident': resident
    })


@login_required
@role_based_access(['manager', 'senior_carer', 'carer'])
def resident_handovers(request, resident_id):

    resident = get_object_or_404(Resident, id=resident_id)

    handovers = resident.handovers.all().order_by('-created_at')

    return render(request, 'carehome/resident_handovers.html', {
        'resident': resident,
        'handovers': handovers
    })


@login_required
@role_based_access(['manager', 'senior_carer'])
def dashboard(request):
    # Get summary info
    residents_count = Resident.objects.count()
    handovers_count = Handover.objects.count()
    recent_handovers = Handover.objects.all().order_by(
        '-created_at'
    )[:5]  # latest 5

    context = {
        'residents_count': residents_count,
        'handovers_count': handovers_count,
        'recent_handovers': recent_handovers,
        'user_role': request.user.role
    }

    return render(request, 'carehome/dashboard.html', context)