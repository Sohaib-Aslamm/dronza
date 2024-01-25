from django.db import models
from django_resized import ResizedImageField

from dronzaPanel.enumeratorts import ServicesCategory


class Gallery(models.Model):
    title = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=100, choices=ServicesCategory.choices, default=ServicesCategory.NATURE)
    description = models.TextField(default="")
    image = ResizedImageField(force_format='JPEG',
                              quality=50, upload_to='Gallery', keep_meta=True, default="")

    class Meta:
        verbose_name_plural = 'Gallery Section'

