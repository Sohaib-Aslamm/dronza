from django.db import models
from django_resized import ResizedImageField


class WhatPeopleSay(models.Model):
    name = models.CharField(max_length=200, default="")
    designation = models.CharField(max_length=200, default="")
    say_something = models.TextField(default="")
    icon = ResizedImageField(force_format='JPEG',
                             quality=30, upload_to='Home/Testimonials', keep_meta=True, default="")

    class Meta:
        verbose_name_plural = 'Testimonial Section'
