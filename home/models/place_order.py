import uuid
from django.db import models
import django.utils.timezone


class Place_Order(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    product_id = models.CharField(max_length=100, default="")
    user_id = models.CharField(max_length=100, default="")
    p_price = models.CharField(max_length=100, default="")
    p_quantity = models.CharField(max_length=100, default="")
    p_total = models.CharField(max_length=100, default="")
    p_grand_total = models.CharField(max_length=100, default="")
    c_name = models.CharField(max_length=100, default="")
    c_email = models.CharField(max_length=100, default="")
    c_phone = models.CharField(max_length=100, default="")
    c_city = models.CharField(max_length=100, default="")
    c_zip = models.CharField(max_length=100, default="")
    c_country = models.CharField(max_length=100, default="")
    c_address1 = models.CharField(max_length=100, default="")
    c_address2 = models.CharField(max_length=100, default="")
    status = models.CharField(max_length=100, default="")
    order_at = models.DateTimeField(default=django.utils.timezone.now)