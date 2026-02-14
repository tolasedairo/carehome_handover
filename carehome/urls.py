from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('residents/', views.residents_list, name='residents_list'),
    path('residents/<int:resident_id>/handovers/', views.resident_handovers, name='resident_handovers'),
    path('residents/<int:resident_id>/add_handover/', views.create_handover, name='create_handover'),
    path('handovers/', views.handover_list, name='handover_list'),
]
