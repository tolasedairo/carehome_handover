from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Dashboard (manager + senior_carer only)
    path('dashboard/', views.dashboard, name='dashboard'),

    # Residents
    path('residents/', views.residents_list, name='residents_list'),
    path('residents/add/', views.add_resident, name='add_resident'),
    path('residents/<int:resident_id>/delete/', views.delete_resident, name='delete_resident'),
    path('residents/delete/', views.bulk_delete_residents, name='bulk_delete_residents'),

    # Resident Handovers
    path('residents/<int:resident_id>/handovers/', views.resident_handovers, name='resident_handovers'),
    path('residents/<int:resident_id>/add_handover/', views.create_handover, name='create_handover'),

    # Resident Care Plans
    path('residents/<int:resident_id>/careplan/', views.manage_careplan, name='manage_careplan'),

    # All Handovers
    path('handovers/', views.handover_list, name='handover_list'),
]
