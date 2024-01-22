from django.db import models


class ServicesType(models.TextChoices):
    REGULAR_SERVICE = 'regular', 'Regular'
    MAIN_SERVICE = 'main', 'Main'


class ServicesCategory(models.TextChoices):
    NATURE = 'nature', 'Nature'
    URBAN = 'urban', 'Urban'
    LANDSCAPE = 'landscape', 'Landscape'
    SPORTS = 'sports', 'Sports'
    SHOOTING = 'shooting', 'Shooting'
    TRAVELING = 'traveling', 'Traveling'

