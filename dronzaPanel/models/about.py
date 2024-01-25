from django.db import models
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField


class HomeAbout(models.Model):
    title = models.CharField(max_length=255, default="")
    description = RichTextField(default="")
    icon = ResizedImageField(force_format='JPEG',
                             quality=80, upload_to='Home_About', keep_meta=True, default="")

    class Meta:
        verbose_name_plural = 'About Section'
