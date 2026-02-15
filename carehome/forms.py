from django import forms
from .models import Handover, Resident, CarePlanSection
from allauth.account.forms import SignupForm, ResetPasswordForm


class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        # Removed 'care_plan' since it's now in CarePlanSection
        fields = ['first_name', 'last_name', 'preferred_name', 'room_number', 'date_of_birth', 'date_of_admission', 'allergies', 'photo']


class HandoverForm(forms.ModelForm):
    class Meta:
        model = Handover
        fields = ['resident', 'shift', 'notes']


# Optional: form to create/edit a CarePlanSection
class CarePlanSectionForm(forms.ModelForm):
    class Meta:
        model = CarePlanSection
        fields = [
            'section_type', 'current_needs', 'desired_outcomes', 'staff_support',
            'date_started', 'end_date', 'ongoing', 'resident_signature'
        ]
        widgets = {
            'date_started': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'current_needs': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'desired_outcomes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'staff_support': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'resident_signature': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })


class CustomResetPasswordForm(ResetPasswordForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email address'
        })
    )
