from django import forms
from .models import Application

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
