from django import forms
from dronzaPanel.models import VideoGallery


class VideoGalleryForm(forms.ModelForm):
    class Meta:
        model = VideoGallery
        fields = '__all__'

        widgets = {
            'video_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter video link'}),
        }