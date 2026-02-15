from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Resident, Handover, CarePlanSection
from .forms import ResidentForm, HandoverForm, CarePlanSectionForm
from .decorators import role_required


# ==============================
# Home Page
# ==============================
def home(request):
    return render(request, "carehome/home.html")


# ==============================
# Residents List View
# ==============================
@login_required
@role_required(['manager', 'senior_carer', 'carer'])
def residents_list(request):
    query = request.GET.get('q', '').strip()

    residents = Resident.objects.all().order_by('last_name', 'first_name')

    if query:
        residents = residents.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(room_number__icontains=query)
        ).distinct()

    paginator = Paginator(residents, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'carehome/residents_list.html', {
        'residents': page_obj,
        'page_obj': page_obj,
        'query': query,
    })


# ==============================
# All Handovers List
# ==============================
@login_required
@role_required(['manager', 'senior_carer', 'carer'])
def handover_list(request):
    user_role = request.user.role

    if user_role in ['manager', 'senior_carer']:
        handovers = Handover.objects.select_related('resident', 'created_by') \
            .order_by('-created_at')
    else:
        handovers = Handover.objects.select_related('resident') \
            .only('resident', 'shift', 'notes', 'created_at') \
            .order_by('-created_at')

    return render(request, 'carehome/handover_list.html', {
        'handovers': handovers
    })


# ==============================
# Create Handover
# ==============================
@login_required
@role_required(['manager', 'senior_carer', 'carer'])
def create_handover(request, resident_id):
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
        form = HandoverForm(initial={'resident': resident})

    return render(request, 'carehome/create_handover.html', {
        'form': form,
        'resident': resident
    })


# ==============================
# Resident Handovers
# ==============================
@login_required
@role_required(['manager', 'senior_carer', 'carer'])
def resident_handovers(request, resident_id):
    resident = get_object_or_404(Resident, id=resident_id)

    handovers = resident.handovers.select_related('created_by') \
        .order_by('-created_at')

    return render(request, 'carehome/resident_handovers.html', {
        'resident': resident,
        'handovers': handovers
    })


# ==============================
# Dashboard (Manager + Senior Only)
# ==============================
@login_required
@role_required(['manager', 'senior_carer'])
def dashboard(request):
    residents_count = Resident.objects.count()
    handovers_count = Handover.objects.count()

    recent_handovers = Handover.objects.select_related('resident') \
        .order_by('-created_at')[:5]

    return render(request, 'carehome/dashboard.html', {
        'residents_count': residents_count,
        'handovers_count': handovers_count,
        'recent_handovers': recent_handovers,
    })


# ==============================
# Manage Care Plan (Structured)
# ==============================
@login_required
@role_required(['manager', 'senior_carer'])
def manage_careplan(request, resident_id):
    resident = get_object_or_404(Resident, id=resident_id)
    sections = resident.care_sections.all()  # Use related_name from model

    if request.method == 'POST':
        form = CarePlanSectionForm(request.POST)
        if form.is_valid():
            section = form.save(commit=False)
            section.resident = resident
            section.save()
            return redirect('manage_careplan', resident_id=resident.id)
    else:
        form = CarePlanSectionForm()

    return render(request, 'carehome/manage_careplan.html', {
        'resident': resident,
        'sections': sections,
        'form': form,
    })


# ==============================
# Add Resident
# ==============================
@login_required
@role_required(['manager'])
def add_resident(request):
    if request.method == 'POST':
        form = ResidentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('residents_list')
    else:
        form = ResidentForm()

    return render(request, 'carehome/add_resident.html', {
        'form': form
    })


# ==============================
# Delete Resident
# ==============================
@login_required
@role_required(['manager'])
def delete_resident(request, resident_id):
    resident = get_object_or_404(Resident, id=resident_id)

    if request.method == 'POST':
        resident.delete()
        return redirect('residents_list')

    return render(request, 'carehome/delete_resident.html', {
        'resident': resident
    })


# ==============================
# Bulk Delete Residents
# ==============================
@login_required
@role_required(['manager'])
def bulk_delete_residents(request):
    if request.method == "POST":
        selected_ids = request.POST.getlist("selected_residents")
        Resident.objects.filter(id__in=selected_ids).delete()

    return redirect("residents_list")
