import uuid
from django.db import models
import django.utils.timezone
from ckeditor.fields import RichTextField
from dronzaPanel.models import Products, droneParts, userBlog
# Create your models here.




droneCategory = (
    ('Metal', 'Metal'),
    ('Fabric', 'Fabric'),
    ('Wireless', 'Wireless'),
    ('Plastic', 'Plastic'),
    ('Titanium', 'Titanium'),
    ('Parts', 'Parts'),
    ('Other', 'Other'),

)

Condition = (
    ('Mint', 'Mint'),
    ('Good', 'Good'),
    ('Excellent', 'Excellent'),


)

yesNo = (
    ('YES', 'YES'),
    ('NO', 'NO'),

)

Featured = (
    ('Featured', 'Featured'),
    ('Not_Featured', 'Not_Featured'),

)

Visible = (
    ('Visible', 'Visible'),
    ('Not_Visible', 'Not_Visible'),
)


class hello(models.Model):
    yourName = models.CharField(max_length=100, default="")
    email = models.EmailField(default="")
    description = models.TextField(default="")


class productReview(models.Model):
    sNo = models.AutoField(primary_key=True)
    author = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200, default="")
    review = models.TextField(default="")
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=django.utils.timezone.now)


class blog_Review(models.Model):
    sNo = models.AutoField(primary_key=True)
    author = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200, default="")
    comment = models.TextField(default="")
    post = models.ForeignKey(userBlog, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=django.utils.timezone.now)
    

class contact_us(models.Model):
    name = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=100, default="")
    subject = models.CharField(max_length=100, default="")
    email = models.EmailField(default="")
    message = models.TextField(default="")
    

class sellYourDrone(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, default="")
    user_id = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=100, default="")
    pPhone = models.EmailField(max_length=100, default="")
    sPhone = models.EmailField(max_length=100, default="")
    location = models.EmailField(max_length=255, default="")
    title = models.CharField(max_length=255, default="")
    price = models.CharField(max_length=100, default="")
    brand = models.CharField(max_length=100, default="")
    color = models.CharField(max_length=100, default="")
    condition = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=100, default="")
    label1 = models.CharField(max_length=100, default="N/A", null=True)
    label2 = models.CharField(max_length=100, default="N/A", null=True)
    label3 = models.CharField(max_length=100, default="N/A", null=True)
    label4 = models.CharField(max_length=100, default="N/A", null=True)
    input1 = models.CharField(max_length=100, default="N/A", null=True)
    input2 = models.CharField(max_length=100, default="N/A", null=True)
    input3 = models.CharField(max_length=100, default="N/A", null=True)
    input4 = models.CharField(max_length=100, default="N/A", null=True)
    description = RichTextField(default="")
    thumbnail = models.FileField(upload_to='sellYourDrone/thumbnail', default="")


class sellYourDroneImages(models.Model):
    def upload_design_to(self, filename):
        return f'sellYourDrone/Product_ID/{self.Product_ID_id}/{filename}'

    Product_ID = models.ForeignKey(sellYourDrone, on_delete=models.CASCADE)
    images = models.FileField(upload_to=upload_design_to)


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

