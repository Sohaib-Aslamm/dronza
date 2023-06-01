from django.db import models
import uuid
from django_resized import ResizedImageField
from ckeditor.fields import RichTextField


class Products(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default="")
    cPrice = models.CharField(max_length=100, default="")
    price = models.CharField(max_length=100, default="")
    currency = models.CharField(max_length=100, default="")
    availability = models.CharField(max_length=100, default="")
    color = models.CharField(max_length=100, default="")
    featured = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=100, default="")
    tags = models.TextField(default="")
    label1 = models.CharField(max_length=100, default="")
    label2 = models.CharField(max_length=100, default="")
    label3 = models.CharField(max_length=100, default="")
    label4 = models.CharField(max_length=100, default="")
    label5 = models.CharField(max_length=100, default="")
    label6 = models.CharField(max_length=100, default="")
    label7 = models.CharField(max_length=100, default="")
    label8 = models.CharField(max_length=100, default="")
    input1 = models.CharField(max_length=100, default="")
    input2 = models.CharField(max_length=100, default="")
    input3 = models.CharField(max_length=100, default="")
    input4 = models.CharField(max_length=100, default="")
    input5 = models.CharField(max_length=100, default="")
    input6 = models.CharField(max_length=100, default="")
    input7 = models.CharField(max_length=100, default="")
    input8 = models.CharField(max_length=100, default="")
    description = RichTextField(default="")
    image = ResizedImageField(size=[320, 180], force_format='PNG', crop=['middle', 'center'], quality=-1,
                              upload_to='DronzaProducts/MainIcon', keep_meta=True, default="")


class productImages(models.Model):
    def upload_design_to(self, filename):
        return f'DronzaProducts/Product_ID/{self.Product_ID_id}/{filename}'

    Product_ID = models.ForeignKey(Products, on_delete=models.CASCADE)
    images = ResizedImageField(size=[1080, 720], force_format='PNG', quality=-1,
                               keep_meta=True, upload_to=upload_design_to)
