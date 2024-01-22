from django.db import models
from django.utils.text import slugify


class EmailContent(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(max_length=200, unique=True, null=True, default=None)
    subject = models.CharField(max_length=255)
    message = models.TextField(null=True, blank=True)
    html_message = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Email Content Section'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
