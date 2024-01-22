from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

from dronzaPanel.enumeratorts import ServicesType


class ServicesTypes(models.Model):
    title = models.CharField(max_length=100, default="")
    slug = models.SlugField(max_length=200, unique=True, null=True, default=None)
    Description = RichTextField(default="")
    quote = models.CharField(max_length=100, default="")
    quote_by = models.CharField(max_length=100, default="")
    type = models.CharField(max_length=100, choices=ServicesType.choices, default=ServicesType.REGULAR_SERVICE)
    icons = models.ImageField(upload_to='services', default="")

    class Meta:
        verbose_name_plural = 'Services Section'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
