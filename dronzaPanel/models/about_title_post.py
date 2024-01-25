from django.db import models
from django_resized import ResizedImageField


class AboutTitlePost(models.Model):
    title = models.CharField(max_length=255, default="")
    description = models.TextField(default="")
    feature1 = models.TextField(default="")
    feature2 = models.TextField(default="")
    feature3 = models.TextField(default="")
    image = ResizedImageField(force_format='JPEG',
                              quality=50, upload_to='about_title_post', keep_meta=True, default="")

    class Meta:
        verbose_name_plural = 'About Title Post'
