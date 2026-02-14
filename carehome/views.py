from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Resident, Handover
from .forms import HandoverForm
from .decorators import role_required


# Home page
def home(request):
    return render(request, "carehome/home.html")


#  Residents views
@login_required
@role_required(['manager', 'senior_carer'])
def residents_list(request):
    """List residents with different info depending on role."""
    user_role = request.user.role

    if user_role == 'manager':
        residents = Resident.objects.all()  # full info
    else:  # senior_carer
        residents = Resident.objects.all().only(
            'id', 'first_name', 'last_name', 'room_number', 'care_plan'
        )

    context = {
        'residents': residents,
        'user_role': user_role
    }
    return render(request, 'carehome/residents_list.html', context)


# Handovers views
@login_required
@role_required(['manager', 'senior_carer', 'carer'])
def handover_list(request):
    """List all handovers depending on user role."""
    user_role = request.user.role

    if user_role in ['manager', 'senior_carer']:
        handovers = Handover.objects.all().order_by('-created_at')
    else:  # carer
        handovers = Handover.objects.all().only(
            'resident', 'shift', 'notes', 'created_at'
        ).order_by('-created_at')

    return render(request, 'carehome/handover_list.html', {
        'handovers': handovers
    })


@login_required
@role_required(['manager', 'senior_carer', 'carer'])
def create_handover(request, resident_id):
    """Create a new handover for a resident."""
    resident = get_object_or_404(Resident, id=resident_id)

    if request.method == 'POST':
        form = HandoverForm(request.POST)
        if form.is_valid():
            handover = form.save(commit=False)
            handover.resident = resident
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
@role_required(['manager', 'senior_carer', 'carer'])
def resident_handovers(request, resident_id):
    """View all handovers for a single resident."""
    resident = get_object_or_404(Resident, id=resident_id)
    handovers = resident.handovers.all().order_by('-created_at')

    return render(request, 'carehome/resident_handovers.html', {
        'resident': resident,
        'handovers': handovers
    })


#  Dashboard view
@login_required
@role_required(['manager', 'senior_carer'])
def dashboard(request):
    """Dashboard showing summary info and recent handovers."""
    residents_count = Resident.objects.count()
    handovers_count = Handover.objects.count()
    recent_handovers = Handover.objects.all().order_by('-created_at')[:5]

    context = {
        'residents_count': residents_count,
        'handovers_count': handovers_count,
        'recent_handovers': recent_handovers,
        'user_role': request.user.role
    }

    return render(request, 'carehome/dashboard.html', context)
