from django import forms
from dronzaPanel.models import Pricing


class PricingForm(forms.ModelForm):
    class Meta:
        model = Pricing
        fields = '__all__'

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter price $100'}),
            'feature1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'feature 1'}),
            'feature2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'feature 1'}),
            'feature3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'feature 1'}),
            'feature4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'feature 1'}),
            'feature5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'feature 1'}),
        }