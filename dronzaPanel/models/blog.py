from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.utils.text import slugify
from django_resized import ResizedImageField


class userBlog(models.Model):
    sNo = models.AutoField(primary_key=True)
    title = models.TextField(default="")
    slug = models.SlugField(max_length=200, unique=True, null=True, default=None)
    heading = models.TextField(default="")
    quote = models.TextField(default="")
    quote_by = models.TextField(default="")
    description = RichTextField(default="")
    Icon = ResizedImageField(size=[720, 405], force_format='JPEG',
                             quality=50, upload_to='Blog/Icons', keep_meta=True, default="")
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Blog Section'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
