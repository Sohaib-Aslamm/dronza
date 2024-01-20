# forms.py
from django import forms
from home.models import sellYourDrone, sellYourDroneImages


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = sellYourDroneImages
        fields = ['image']


ProductImageFormSet = forms.inlineformset_factory(sellYourDrone, sellYourDroneImages, form=ProductImageForm, extra=1)
