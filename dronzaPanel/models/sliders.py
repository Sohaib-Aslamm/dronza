from django.db import models
from django_resized import ResizedImageField


class MainSlider(models.Model):
    title = models.CharField(max_length=200, default="")
    page = models.CharField(max_length=200, default="")
    image = ResizedImageField(size=[1920, 500], force_format='JPEG',
                              quality=50, upload_to='Main_Page_Slider_Image', keep_meta=True, default="")

    class Meta:
        verbose_name_plural = 'Page Slider Section'
