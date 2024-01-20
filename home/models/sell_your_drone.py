import uuid
from django.db import models
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField
from django.utils.text import slugify
from django.contrib.auth.models import User
from home.enumerators import DRONE_CATEGORY, SOLD_STATUS, DRONE_COLOR, DRONE_CONDITION, DRONE_BRAND


class sellYourDrone(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    email = models.EmailField(max_length=100, default="")
    pPhone = models.CharField(max_length=100, default="")
    sPhone = models.CharField(max_length=100, null=True, default="")
    address = models.CharField(max_length=255, default="")
    location = models.CharField(max_length=255, default="")
    title = models.CharField(max_length=255, default="")
    slug = models.SlugField(max_length=200, unique=True, null=True, default=None)
    price = models.CharField(max_length=100, default="")
    brand = models.CharField(max_length=100, default=DRONE_BRAND.DRONZA, choices=DRONE_BRAND.choices)
    color = models.CharField(max_length=100, default=DRONE_COLOR.WHITE, choices=DRONE_COLOR.choices)
    condition = models.CharField(max_length=100, default=DRONE_CONDITION.EXCELLENT, choices=DRONE_CONDITION.choices)
    category = models.CharField(max_length=100, default=DRONE_CATEGORY.OTHER, choices=DRONE_CATEGORY.choices)
    status = models.CharField(max_length=100, default=SOLD_STATUS.AVAILABLE, choices=SOLD_STATUS.choices)
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
    is_featured = models.BooleanField(default=False, verbose_name='Is Featured Product')

    class Meta:
        verbose_name_plural = 'User Products'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class sellYourDroneImages(models.Model):
    def resource_location(self, filename):
        return f'sellYourDrone/{self.Product.name}/{filename}'

    Product = models.ForeignKey(sellYourDrone, on_delete=models.CASCADE)
    image = ResizedImageField(size=[1080, 720], force_format='PNG', upload_to=resource_location)

    class Meta:
        verbose_name_plural = 'User Products Images'
