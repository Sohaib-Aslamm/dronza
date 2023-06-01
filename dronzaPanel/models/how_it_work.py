from django.db import models


class HomeHIW(models.Model):
    title = models.CharField(max_length=255, default="")
    description = models.TextField(default="")
    image = models.ImageField(upload_to='Home_HowITWORK', default="")