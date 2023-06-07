from django.db import models
from django.utils.text import slugify

ServiceType = (
    ('RegularService', 'RegularService'),
    ('MainService', 'MainService'),
)


class ServicesTypes(models.Model):
    title = models.CharField(max_length=100, default="")
    slug = models.SlugField(max_length=200, unique=True, null=True, default=None)
    Description = models.TextField(default="")
    quote = models.CharField(max_length=100, default="")
    quote_by = models.CharField(max_length=100, default="")
    type = models.CharField(max_length=100, choices=ServiceType, default="")
    highlight1 = models.CharField(max_length=100, default="")
    highlight2 = models.CharField(max_length=100, default="")
    highlight3 = models.CharField(max_length=100, default="")
    highlight4 = models.CharField(max_length=100, default="")
    highlight5 = models.CharField(max_length=100, default="")
    highlight6 = models.CharField(max_length=100, default="")
    icons = models.ImageField(upload_to='services', default="")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
