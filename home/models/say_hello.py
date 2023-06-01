from django.db import models


class hello(models.Model):
    yourName = models.CharField(max_length=100, default="")
    email = models.EmailField(default="")
    description = models.TextField(default="")