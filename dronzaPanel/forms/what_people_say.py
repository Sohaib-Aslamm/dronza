from django import forms
from dronzaPanel.models import WhatPeopleSay


class WhatPeopleSForm(forms.ModelForm):
    class Meta:
        model = WhatPeopleSay
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter name'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your designation'}),
            'say_something': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Say Something'}),
        }