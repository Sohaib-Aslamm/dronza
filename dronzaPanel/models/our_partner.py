from django.db import models


class OurPartner(models.Model):
    company_name = models.CharField(max_length=200, default="")
    description = models.TextField(default="")
    logo = models.ImageField(upload_to='Home/Partners', default="")

    class Meta:
        verbose_name_plural = 'Our Partner Section'
