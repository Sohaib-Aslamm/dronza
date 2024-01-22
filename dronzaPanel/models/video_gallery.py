from django.db import models


class VideoGallery(models.Model):
    video_link = models.CharField(max_length=200, default="")
    icon = models.ImageField(upload_to='Home/Video_Gallery', default="")

    class Meta:
        verbose_name_plural = 'Video Gallery Section'
