from django.db import models
from dronzaPanel.models import Products
import django.utils.timezone


class productReview(models.Model):
    sNo = models.AutoField(primary_key=True)
    author = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200, default="")
    review = models.TextField(default="")
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=django.utils.timezone.now)
