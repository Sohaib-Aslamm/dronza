from django import forms
from dronzaPanel.models import HomeHIW


class HomeHIWForm(forms.ModelForm):
    class Meta:
        model = HomeHIW
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter description'}),
        }
