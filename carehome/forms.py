from django import forms
from .models import Handover, Resident, CarePlanSection
from allauth.account.forms import SignupForm, ResetPasswordForm


# ==============================
# Resident Form
# ==============================
class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        # Removed 'care_plan' since it's now in CarePlanSection
        fields = [
            'first_name',
            'last_name',
            'preferred_name',
            'room_number',
            'date_of_birth',
            'date_of_admission',
            'allergies',
            'photo',
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_of_admission': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'preferred_name': forms.TextInput(attrs={'class': 'form-control'}),
            'room_number': forms.TextInput(attrs={'class': 'form-control'}),
            'allergies': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


# ==============================
# Handover Form
# ==============================
class HandoverForm(forms.ModelForm):
    class Meta:
        model = Handover
        fields = ['resident', 'shift', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'shift': forms.Select(attrs={'class': 'form-control'}),
            'resident': forms.HiddenInput(),  # hidden when assigned in view
        }


# ==============================
# Care Plan Section Form
# ==============================
class CarePlanSectionForm(forms.ModelForm):
    class Meta:
        model = CarePlanSection
        fields = [
            'section_type',
            'current_needs',
            'desired_outcomes',
            'staff_support',
            'date_started',
            'end_date',
            'ongoing',
            'resident_signature'
        ]
        widgets = {
            'section_type': forms.Select(attrs={'class': 'form-control'}),
            'current_needs': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'desired_outcomes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'staff_support': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'date_started': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'resident_signature': forms.TextInput(attrs={'class': 'form-control'}),
        }


# ==============================
# Allauth Custom Forms
# ==============================
class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class CustomResetPasswordForm(ResetPasswordForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email address'
        })
    )
