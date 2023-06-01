from django import forms
from dronzaPanel.models import SocialMedia


class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = SocialMedia
        fields = '__all__'

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'enter email'}),
            'skype': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter skype'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(+92) 344 4276747'}),
            'github': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'paste github link'}),
            'linkedin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'paste linkedin link'}),
            'google_plus': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'paste google+ link'}),
            'youtube': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'paste youtube link'}),
            'facebook': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'paste facebook link'}),
            'twitter': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'paste twitter link'}),
        }

