from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField


class OurTeam(models.Model):
    name = models.CharField(max_length=100, default="")
    slug = models.SlugField(max_length=200, unique=True, null=True, default=None)
    email = models.EmailField(max_length=100, default="")
    phone = models.CharField(max_length=100, default="")
    experience = models.CharField(max_length=100, default="")
    designation = models.CharField(max_length=100, default="")
    social_name_1 = models.CharField(max_length=100, default="")
    social_link_1 = models.CharField(max_length=200, default="")
    social_name_2 = models.CharField(max_length=100, default="")
    social_link_2 = models.CharField(max_length=200, default="")
    social_name_3 = models.CharField(max_length=100, default="")
    social_link_3 = models.CharField(max_length=200, default="")
    description = RichTextField(default="")
    profile = ResizedImageField(force_format='JPEG',
                                quality=50, upload_to='our_team', keep_meta=True, default="")

    class Meta:
        verbose_name_plural = 'Our Team Section'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
