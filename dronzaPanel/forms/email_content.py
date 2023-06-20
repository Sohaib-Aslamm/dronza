from django import forms
from dronzaPanel.models import EmailContent


class EmailContentForm(forms.ModelForm):
    class Meta:
        model = EmailContent
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter name'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'text message'}),
            'html_message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'html text'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slug'].required = False