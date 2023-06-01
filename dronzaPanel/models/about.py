from django.db import models


class HomeAbout(models.Model):
    title = models.CharField(max_length=255, default="")
    description = models.TextField(default="")
    feature1 = models.CharField(max_length=100, default="")
    feature2 = models.CharField(max_length=100, default="")
    feature3 = models.CharField(max_length=100, default="")
    icon = models.ImageField(upload_to='Home_About', default="")