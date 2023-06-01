from django import forms
from dronzaPanel.models import MainSlider


class MainSliderForm(forms.ModelForm):
    class Meta:
        model = MainSlider
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'header': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter header'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter description'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '$100'}),
        }