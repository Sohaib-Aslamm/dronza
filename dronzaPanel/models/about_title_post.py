from django.db import models


class AboutTitlePost(models.Model):
    title = models.CharField(max_length=255, default="")
    description = models.TextField(default="")
    feature1 = models.TextField(default="")
    feature2 = models.TextField(default="")
    feature3 = models.TextField(default="")
    image = models.ImageField(upload_to='about_title_post', default="")

    class Meta:
        verbose_name_plural = 'About Title Post'
