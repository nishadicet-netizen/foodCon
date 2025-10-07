# forms.py
from django import forms
from foodconapp.models import RegistrationForm

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)

    class Meta:
        model = RegistrationForm
        fields = ['first_name', 'last_name', 'place', 'phone', 'email', 'username', 'password']
