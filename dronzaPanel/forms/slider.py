from django import forms
from dronzaPanel.models import MainSlider


class MainSliderForm(forms.ModelForm):
    class Meta:
        model = MainSlider
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'page': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter page name'}),
        }