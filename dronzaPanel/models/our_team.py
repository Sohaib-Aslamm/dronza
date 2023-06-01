from django.db import models


class OurTeam(models.Model):
    name = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=100, default="")
    phone = models.CharField(max_length=100, default="")
    experience = models.CharField(max_length=100, default="")
    designation = models.CharField(max_length=100, default="")
    socialmedia1 = models.CharField(max_length=100, default="")
    socialmedia2 = models.CharField(max_length=100, default="")
    socialmedia3 = models.CharField(max_length=100, default="")
    description = models.TextField(default="")
    profile = models.ImageField(upload_to='our_team', default="")