from django import forms
from dronzaPanel.models import HomeAbout


class HomeAboutForm(forms.ModelForm):
    class Meta:
        model = HomeAbout
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter description'}),
            'feature1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter feature 1'}),
            'feature2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter feature 2'}),
            'feature3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter feature 3'}),
        }