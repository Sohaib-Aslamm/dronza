from django import forms
from home.models import contact_us


class contactForm(forms.ModelForm):
    class Meta:
        model = contact_us
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name', 'autocomplete': 'off',
                                           'style': "border: 1px solid #000000;"}),

            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject', 'autocomplete': 'off',
                                           'style': "border: 1px solid #000000;"}),

            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone', 'autocomplete': 'off',
                                           'style': "border: 1px solid #000000;"}),

            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your valid Email',
                                             'autocomplete': 'off', 'style': "border: 1px solid #000000;"}),

            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'autocomplete': 'off',
                                           'style': "border: 1px solid #000000;"}),
        }