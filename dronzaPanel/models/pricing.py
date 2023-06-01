from django.db import models


category = (
    ('Nature', 'Nature'),
    ('Urbanistic', 'Urbanistic'),
    ('Landscape', 'Landscape'),
    ('Sports', 'Sports'),
    ('Shooting', 'Shooting'),
    ('Traveling', 'Traveling'),
)


class Pricing(models.Model):
    category = models.CharField(max_length=255, choices=category, default="")
    price = models.CharField(max_length=255, default="")
    feature1 = models.CharField(max_length=255, default="")
    feature2 = models.CharField(max_length=255, default="")
    feature3 = models.CharField(max_length=255, default="")
    feature4 = models.CharField(max_length=255, default="")
    feature5 = models.CharField(max_length=255, default="")