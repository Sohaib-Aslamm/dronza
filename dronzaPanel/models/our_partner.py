from django.db import models
from django_resized import ResizedImageField


class OurPartner(models.Model):
    company_name = models.CharField(max_length=200, default="")
    description = models.TextField(default="")
    logo = ResizedImageField(force_format='JPEG',
                             quality=80, upload_to='Home/Partners', keep_meta=True, default="")

    class Meta:
        verbose_name_plural = 'Our Partner Section'
