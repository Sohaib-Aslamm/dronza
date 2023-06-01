from django import forms
from dronzaPanel.models import QualityTrust


class QualityTrustForm(forms.ModelForm):
    class Meta:
        model = QualityTrust
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'Description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter description'}),
        }