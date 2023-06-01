from django.db import models


class SocialMedia(models.Model):
    email = models.EmailField(max_length=255, default="")
    skype = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=255, default="")
    github = models.CharField(max_length=255, default="")
    linkedin = models.CharField(max_length=255, default="")
    google_plus = models.CharField(max_length=255, default="")
    youtube = models.CharField(max_length=255, default="")
    facebook = models.CharField(max_length=255, default="")
    twitter = models.CharField(max_length=255, default="")