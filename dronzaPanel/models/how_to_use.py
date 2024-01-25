from django.db import models
from django_resized import ResizedImageField


class HomeHTU(models.Model):
    title = models.CharField(max_length=255, default="")
    description = models.TextField(default="")
    icon = ResizedImageField(force_format='JPEG',
                             quality=50, upload_to='Home_HowToUse', keep_meta=True, default="")

    class Meta:
        verbose_name_plural = 'How to Use Section'
