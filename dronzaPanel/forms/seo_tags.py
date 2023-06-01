from django import forms
from dronzaPanel.models import seoTags


class SEOTagsForm(forms.ModelForm):
    class Meta:
        model = seoTags
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'page': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter page name'}),
            'canonical_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter canonical_link'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter description'}),
            'tags': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter #tags'}),
        }
