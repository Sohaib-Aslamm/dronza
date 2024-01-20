from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'placeholder': 'enter valid e-mail'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'choose password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'confirm password'}),
        }
