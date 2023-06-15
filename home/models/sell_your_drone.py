import uuid
from django.db import models
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField
from django.utils.text import slugify


class sellYourDrone(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, default="")
    user_id = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=100, default="")
    pPhone = models.EmailField(max_length=100, default="")
    sPhone = models.EmailField(max_length=100, null=True, default="")
    location = models.EmailField(max_length=255, default="")
    title = models.CharField(max_length=255, default="")
    slug = models.SlugField(max_length=200, unique=True, null=True, default=None)
    price = models.CharField(max_length=100, default="")
    brand = models.CharField(max_length=100, default="")
    color = models.CharField(max_length=100, default="")
    condition = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=100, default="")
    status = models.CharField(max_length=100, default="")
    label1 = models.CharField(max_length=100, default="N/A", null=True)
    label2 = models.CharField(max_length=100, default="N/A", null=True)
    label3 = models.CharField(max_length=100, default="N/A", null=True)
    label4 = models.CharField(max_length=100, default="N/A", null=True)
    input1 = models.CharField(max_length=100, default="N/A", null=True)
    input2 = models.CharField(max_length=100, default="N/A", null=True)
    input3 = models.CharField(max_length=100, default="N/A", null=True)
    input4 = models.CharField(max_length=100, default="N/A", null=True)
    description = RichTextField(default="")
    thumbnail = ResizedImageField(size=[320, 180], force_format='PNG',
                                  quality=-1, upload_to='sellYourDrone/thumbnail', keep_meta=True, default="")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class sellYourDroneImages(models.Model):
    def upload_design_to(self, filename):
        return f'sellYourDrone/Product_ID/{self.Product_ID_id}/{filename}'

    Product_ID = models.ForeignKey(sellYourDrone, on_delete=models.CASCADE)
    images = ResizedImageField(size=[1080, 720], force_format='PNG', upload_to=upload_design_to)