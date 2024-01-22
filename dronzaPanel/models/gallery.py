from django.db import models
from dronzaPanel.enumeratorts import ServicesCategory


class Gallery(models.Model):
    title = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=100, choices=ServicesCategory.choices, default=ServicesCategory.NATURE)
    description = models.TextField(default="")
    image = models.ImageField(upload_to='Gallery', default="")

    class Meta:
        verbose_name_plural = 'Gallery Section'

