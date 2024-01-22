from django.db import models


class QualityTrust(models.Model):
    title = models.CharField(max_length=255, default="")
    Description = models.TextField(default="")
    icon = models.ImageField(upload_to='about_quality_trust', default="")

    class Meta:
        verbose_name_plural = 'About Quality Trust Section'
