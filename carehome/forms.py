from django import forms
from .models import Handover
from allauth.account.forms import SignupForm, ResetPasswordForm


class HandoverForm(forms.ModelForm):
    class Meta:
        model = Handover
        fields = ['resident', 'shift', 'notes']


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
