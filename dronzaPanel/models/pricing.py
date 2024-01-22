from django.db import models

from dronzaPanel.enumeratorts import ServicesCategory


class Pricing(models.Model):
    category = models.CharField(max_length=255, choices=ServicesCategory.choices, default=ServicesCategory.NATURE)
    price = models.CharField(max_length=255, default="")
    feature1 = models.CharField(max_length=255, default="")
    feature2 = models.CharField(max_length=255, default="")
    feature3 = models.CharField(max_length=255, default="")
    feature4 = models.CharField(max_length=255, default="")
    feature5 = models.CharField(max_length=255, default="")
