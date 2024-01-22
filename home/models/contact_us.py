from django.db import models


class contact_us(models.Model):
    name = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=100, default="")
    subject = models.CharField(max_length=100, default="")
    email = models.EmailField(default="")
    message = models.TextField(default="")

    class Meta:
        verbose_name_plural = 'Contact Us (Messages)'
