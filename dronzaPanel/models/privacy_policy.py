from django.db import models
from ckeditor.fields import RichTextField


class PrivacyPolicy(models.Model):
    title = models.TextField(default="")
    heading = models.TextField(default="")
    description = RichTextField(default="")

    class Meta:
        verbose_name_plural = 'Privacy Policy'
