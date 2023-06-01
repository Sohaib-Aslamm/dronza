from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter user name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'placeholder': 'Enter valid mail to get notifications'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'choose password'}),
            'password2': forms.PasswordInput( attrs={'class': 'form-control', 'placeholder': 'confirm password'}),
        }