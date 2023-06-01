from django import forms
from dronzaPanel.models import Gallery


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'Category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'select category'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter description'}),

        }
