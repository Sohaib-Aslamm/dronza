from django.db import models
from django_resized import ResizedImageField


class QualityTrust(models.Model):
    title = models.CharField(max_length=255, default="")
    Description = models.TextField(default="")
    icon = ResizedImageField(force_format='JPEG',
                             quality=80, upload_to='about_quality_trust', keep_meta=True, default="")

    class Meta:
        verbose_name_plural = 'About Quality Trust Section'
