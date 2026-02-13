"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from carehome.views import home, residents_list
from carehome.views import handover_list
from carehome.views import create_handover
from carehome.views import resident_handovers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Allauth login/logout/signup
    path('', home, name='home'),  # root route
    path('residents/', residents_list, name='residents_list'),
    path('handovers/', handover_list, name='handover_list'),
    path('handovers/create/', create_handover, name='create_handover'),
    path('residents/<int:resident_id>/handovers/', resident_handovers, name='resident_handovers'),
    path('residents/<int:resident_id>/add_handover/', create_handover, name='create_handover'),
]
