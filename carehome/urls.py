from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Dashboard (manager and senior_carer only)
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Add and delete residents (manager only)
    path('residents/add/', views.add_resident, name='add_resident'),
    path('residents/<int:resident_id>/delete/', views.delete_resident, name='delete_resident'),  
    
    # Bulk delete residents (manager only)
    path('residents/delete/', views.bulk_delete_residents, name='bulk_delete_residents'),


    # Residents
    path('residents/', views.residents_list, name='residents_list'),
    path('residents/<int:resident_id>/handovers/', views.resident_handovers, name='resident_handovers'),
    path('residents/<int:resident_id>/add_handover/', views.create_handover, name='create_handover'),

    # Care Plans
    path('residents/<int:resident_id>/careplan/', views.manage_careplan, name='manage_careplan'),

    # Handovers
    path('handovers/', views.handover_list, name='handover_list'),
    
]



