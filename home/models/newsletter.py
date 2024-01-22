from django.db import models
import django.utils.timezone


class NewsLetterSubscriber(models.Model):
    email = models.EmailField(default="")
    timestamp = models.DateTimeField(default=django.utils.timezone.now)
