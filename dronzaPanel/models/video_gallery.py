from django.db import models
from django_resized import ResizedImageField


class VideoGallery(models.Model):
    video_link = models.CharField(max_length=200, default="")
    icon = ResizedImageField(force_format='JPEG',
                             quality=50, upload_to='Home/Video_Gallery', keep_meta=True, default="")

    class Meta:
        verbose_name_plural = 'Video Gallery Section'
