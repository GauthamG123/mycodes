# forms.py
from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your firstname'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your lastname'}))
    email = forms.EmailField(max_length=100, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter your email id'}))
    password = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
    password1 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter password'}))
