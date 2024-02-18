from django import forms
from home.models import contact_us


class contactForm(forms.ModelForm):
    class Meta:
        model = contact_us
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'autocomplete': 'off'}),

            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject', 'autocomplete': 'off'}),

            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone', 'autocomplete': 'off'}),

            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),

            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'autocomplete': 'off'}),
        }
