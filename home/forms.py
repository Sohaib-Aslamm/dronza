from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from home.models import contact_us, blog_Review




class contactForm(forms.ModelForm):
    class Meta:
        model = contact_us
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name','autocomplete':'off'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject','autocomplete':'off'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone','autocomplete':'off'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email','autocomplete':'off'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message','autocomplete':'off'}),
        }


class commentForm(forms.ModelForm):
    class Meta:
        model = blog_Review
        fields = '__all__'

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment'}),
        }