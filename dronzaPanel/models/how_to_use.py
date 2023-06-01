from django.db import models


class HomeHTU(models.Model):
    title = models.CharField(max_length=255, default="")
    description = models.TextField(default="")
    icon = models.ImageField(upload_to='Home_HowToUse', default="")