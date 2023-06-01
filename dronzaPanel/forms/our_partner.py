from django import forms
from dronzaPanel.models import OurPartner


class OurPartnerForm(forms.ModelForm):
    class Meta:
        model = OurPartner
        fields = '__all__'

        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'company name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'company introduction'}),
        }