from django import forms
from dronzaPanel.models import userBlog


class userBlogForm(forms.ModelForm):
    class Meta:
        model = userBlog
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'heading': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter heading'}),
            'tags': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'enter tags ex. (IT, Business, Accounts)'}),
            'quote': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter a "Quote" regarding post'}),
            'quote_by': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'who said this quote ex. (sohaib_langrial)'}),


        }
