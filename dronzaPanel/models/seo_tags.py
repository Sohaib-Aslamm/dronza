from django.db import models


class seoTags(models.Model):
    title = models.TextField(default="")
    page = models.TextField(default="")
    canonical_link = models.TextField(default="")
    description = models.TextField(default="")
    tags = models.TextField(default="")
