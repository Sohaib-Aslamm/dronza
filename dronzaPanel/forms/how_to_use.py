from django import forms
from dronzaPanel.models import HomeHTU


class HomeHTUForm(forms.ModelForm):
    class Meta:
        model = HomeHTU
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter description'}),
        }
