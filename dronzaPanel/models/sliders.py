from django.db import models


class MainSlider(models.Model):
    title = models.CharField(max_length=200, default="")
    page = models.CharField(max_length=200, default="")
    image = models.ImageField(upload_to='Main_Page_Slider_Image', default="")
    background_image = models.ImageField(upload_to='Main_Page_Slider_Background', default="")

    class Meta:
        verbose_name_plural = 'Page Slider Section'
