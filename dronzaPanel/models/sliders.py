from django.db import models


class MainSlider(models.Model):
    title = models.CharField(max_length=100, default="")
    header = models.TextField(default="")
    description = models.TextField(default="")
    price = models.TextField(default="")
    image = models.ImageField(upload_to='Home_Main_Slider', default="")
    backImage = models.ImageField(upload_to='slide_back_Image', default="")