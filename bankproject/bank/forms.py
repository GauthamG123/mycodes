from django import forms
from django.forms import DateInput
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'dob', 'age', 'gender', 'phone_number', 'email', 'address', 'district', 'branch','account_type', 'debit_card', 'credit_card', 'cheque_book']
        widgets = {
                    'dob': DateInput(attrs={'type': 'date'}),
                }
