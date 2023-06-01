from django import forms
from dronzaPanel.models import ServicesTypes


class ServicesTypeForm(forms.ModelForm):
    class Meta:
        model = ServicesTypes
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'quote': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'write quote'}),
            'quote_by': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'quote author'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'highlight1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'high light 1'}),
            'highlight2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'high light 2'}),
            'highlight3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'high light 3'}),
            'highlight4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'high light 4'}),
            'highlight5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'high light 5'}),
            'highlight6': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'high light 6'}),
            'Description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter description'}),
        }
