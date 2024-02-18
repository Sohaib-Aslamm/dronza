from django.db import models


class OpeningHours(models.Model):
    from_to_day = models.CharField(max_length=255, null=True, blank=True)
    close_one = models.CharField(max_length=255, blank=True, null=True)
    close_two = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Dronza Opening Hours'
