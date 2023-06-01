from django import forms
from dronzaPanel.models import OurTeam


class OurTeamForm(forms.ModelForm):
    class Meta:
        model = OurTeam
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'team member name'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'member designation'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'member@dronza.org'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+92 xxx xxxxxxx'}),
            'experience': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '5+ Year'}),
            'socialmedia1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Linkedin'}),
            'socialmedia2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Facebook'}),
            'socialmedia3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Twitter'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'write member detail...'}),
        }
