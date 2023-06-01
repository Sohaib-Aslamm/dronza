from django.db import models


class HomeSRFP(models.Model):
    satisfied_clients = models.CharField(max_length=100, default="")
    resolution = models.CharField(max_length=100, default="")
    flight_time = models.CharField(max_length=100, default="")
    project_done = models.CharField(max_length=100, default="")
