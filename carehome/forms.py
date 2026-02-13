from django import forms
from .models import Handover


class HandoverForm(forms.ModelForm):
    class Meta:
        model = Handover
        fields = ['resident', 'shift', 'notes']