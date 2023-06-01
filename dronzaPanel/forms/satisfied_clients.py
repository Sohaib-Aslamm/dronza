from django import forms
from dronzaPanel.models import HomeSRFP


class HomeSRFPForm(forms.ModelForm):
    class Meta:
        model = HomeSRFP
        fields = '__all__'

        widgets = {
            'satisfied_clients': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. 60 or 70'}),
            'resolution': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. 4K , 8K'}),
            'flight_time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. 45 minute'}),
            'project_done': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. 100'}),
        }
