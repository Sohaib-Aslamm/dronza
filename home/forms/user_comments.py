from django import forms
from home.models import blog_Review


class commentForm(forms.ModelForm):
    class Meta:
        model = blog_Review
        fields = '__all__'

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment'}),
        }