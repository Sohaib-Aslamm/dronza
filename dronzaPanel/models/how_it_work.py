from django.db import models
from django_resized import ResizedImageField


class HomeHIW(models.Model):
    title = models.CharField(max_length=255, default="")
    description = models.TextField(default="")
    image = ResizedImageField(force_format='JPEG',
                              quality=80, upload_to='Home_HowITWORK', keep_meta=True, default="")

    class Meta:
        verbose_name_plural = 'How it Work Section'
