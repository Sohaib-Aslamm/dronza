from django.db import models

category = (
    ('Nature', 'Nature'),
    ('Urbanistic', 'Urbanistic'),
    ('Landscape', 'Landscape'),
    ('Sports', 'Sports'),
    ('Shooting', 'Shooting'),
    ('Traveling', 'Traveling'),
)


class Gallery(models.Model):
    title = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=100, choices=category, default="")
    description = models.TextField(default="")
    image = models.ImageField(upload_to='Gallery', default="")
