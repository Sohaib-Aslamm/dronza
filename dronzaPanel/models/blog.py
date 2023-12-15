from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.utils.text import slugify


class userBlog(models.Model):
    sNo = models.AutoField(primary_key=True)
    title = models.TextField(default="")
    slug = models.SlugField(max_length=200, unique=True, null=True, default=None)
    heading = models.TextField(default="")
    tags = models.TextField(default="")
    quote = models.TextField(default="")
    quote_by = models.TextField(default="")
    description = RichTextField(default="")
    Icon = models.ImageField(upload_to='Blog/Icons', default="")
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
