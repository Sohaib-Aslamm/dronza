from django.db import models
from ckeditor.fields import RichTextField


class HomeAbout(models.Model):
    title = models.CharField(max_length=255, default="")
    description = RichTextField(default="")
    icon = models.ImageField(upload_to='Home_About', default="")
