from django.core import validators
from django import forms
from .models import Crud_Users

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Crud_Users
        fields = ['name','email','password']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }