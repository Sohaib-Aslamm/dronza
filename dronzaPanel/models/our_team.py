from django.db import models
from django.utils.text import slugify


class OurTeam(models.Model):
    name = models.CharField(max_length=100, default="")
    slug = models.SlugField(max_length=200, unique=True, null=True, default=None)
    email = models.EmailField(max_length=100, default="")
    phone = models.CharField(max_length=100, default="")
    experience = models.CharField(max_length=100, default="")
    designation = models.CharField(max_length=100, default="")
    socialmedia1 = models.CharField(max_length=100, default="")
    socialmedia2 = models.CharField(max_length=100, default="")
    socialmedia3 = models.CharField(max_length=100, default="")
    description = models.TextField(default="")
    profile = models.FileField(upload_to='our_team', default="")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
