import uuid
import os
import django.utils.timezone
from django.db import models
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField

from django.conf import settings

BASE_DIR = settings.BASE_DIR

# Create your models here.

category = (
    ('Nature', 'Nature'),
    ('Urbanistic', 'Urbanistic'),
    ('Landscape', 'Landscape'),
    ('Sports', 'Sports'),
    ('Shooting', 'Shooting'),
    ('Traveling', 'Traveling'),
)

droneCategory = (
    ('Metal', 'Metal'),
    ('Fabric', 'Fabric'),
    ('Wireless', 'Wireless'),
    ('Plastic', 'Plastic'),
    ('Titanium', 'Titanium'),
    ('Featured', 'Featured'),
    ('Aluminium', 'Aluminium'),
    ('Parts', 'Parts'),
    ('Other', 'Other'),

)

yesNo = (
    ('YES', 'YES'),
    ('NO', 'NO'),

)

Featured = (
    ('Featured', 'Featured'),
    ('Not_Featured', 'Not_Featured'),

)

inStock = (
    ('In Stock', 'In Stock'),
    ('Out of Stock', 'Out of Stock'),
)


DroneColor = (
    ('RED', 'RED'),
    ('GREEN', 'GREEN'),
    ('BLUE', 'BLUE'),
    ('BLACK', 'BLACK'),

)

DroneSize = (
    ('Small', 'Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large'),
    ('Extra Large', 'Extra Large'),

)

partCategory = (
    ('Frame', 'Frame'),
    ('Motor', 'Motor'),
    ('ESC', 'ESC'),
    ('FC Board', 'FC Board'),
    ('Propeller', 'Propeller'),
    ('Transmitter', 'Transmitter'),
    ('Battery', 'Battery'),
    ('Cables', 'Cables'),
    ('Camera', 'Camera'),
    ('Gears', 'Gears'),
)


DroneWarranty = (
    ('6 Month', '6 Month'),
    ('1 Year', '1 Year'),
    ('2 Year', '2 Year'),
    ('5 Year', '5 Year'),

)

ServiceType = (
    ('RegularService', 'RegularService'),
    ('MainService', 'MainService'),
)


class AboutTitlePost(models.Model):
    title = models.CharField(max_length=255, default="")
    description = models.TextField(default="")
    feature1 = models.TextField(default="")
    feature2 = models.TextField(default="")
    feature3 = models.TextField(default="")
    image = models.ImageField(upload_to='about_title_post', default="")


class MainSlider(models.Model):
    title = models.CharField(max_length=100, default="")
    header = models.TextField(default="")
    description = models.TextField(default="")
    price = models.TextField(default="")
    image = models.ImageField(upload_to='Home_Main_Slider', default="")
    backImage = models.ImageField(upload_to='slide_back_Image', default="")


class HomeHIW(models.Model):
    title = models.CharField(max_length=255, default="")
    description = models.TextField(default="")
    image = models.ImageField(upload_to='Home_HowITWORK', default="")


class HomeHTU(models.Model):
    title = models.CharField(max_length=255, default="")
    description = models.TextField(default="")
    icon = models.ImageField(upload_to='Home_HowToUse', default="")


class HomeAbout(models.Model):
    title = models.CharField(max_length=255, default="")
    description = models.TextField(default="")
    feature1 = models.CharField(max_length=100, default="")
    feature2 = models.CharField(max_length=100, default="")
    feature3 = models.CharField(max_length=100, default="")
    icon = models.ImageField(upload_to='Home_About', default="")


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


class droneParts(models.Model):
    name = models.CharField(max_length=255, default="")
    cPrice = models.CharField(max_length=100, default="")
    price = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=100, choices=partCategory, default="")
    color = models.CharField(max_length=100, default="")
    currency = models.CharField(max_length=100, default="")
    availability = models.CharField(max_length=100, choices=inStock, default="")
    featured = models.CharField(max_length=100, choices=Featured, default="")
    label1 = models.CharField(max_length=100, default="")
    label2 = models.CharField(max_length=100, default="")
    label3 = models.CharField(max_length=100, default="")
    label4 = models.CharField(max_length=100, default="")
    label5 = models.CharField(max_length=100, default="")
    label6 = models.CharField(max_length=100, default="")
    input1 = models.CharField(max_length=100, default="")
    input2 = models.CharField(max_length=100, default="")
    input3 = models.CharField(max_length=100, default="")
    input4 = models.CharField(max_length=100, default="")
    input5 = models.CharField(max_length=100, default="")
    input6 = models.CharField(max_length=100, default="")
    description = models.TextField(default="")
    image = models.FileField(upload_to='DroneParts/Thumbnail', default="")


class amazonProduct(models.Model):
    sNo = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, default="")


class productImages(models.Model):
    def upload_design_to(self, filename):
        return f'DronzaProducts/Product_ID/{self.Product_ID_id}/{filename}'

    Product_ID = models.ForeignKey(Products, on_delete=models.CASCADE)
    images = ResizedImageField(size=[1080, 720], force_format='PNG', quality=-1,
                               keep_meta=True, upload_to=upload_design_to)


class amazonProductImages(models.Model):
    def upload_design_to(self, filename):
        return f'AmazonProducts/Product_ID/{self.Product_ID_id}/{filename}'

    Product_ID = models.ForeignKey(amazonProduct, on_delete=models.CASCADE)
    images = models.FileField(upload_to=upload_design_to)


class dronePartsImages(models.Model):
    def upload_design_to(self, filename):
        return f'DroneParts/Product_ID/{self.Product_ID_id}/{filename}'

    Product_ID = models.ForeignKey(droneParts, on_delete=models.CASCADE)
    images = models.FileField(upload_to=upload_design_to)


class QualityTrust(models.Model):
    title = models.CharField(max_length=255, default="")
    Description = models.TextField(default="")
    icon = models.ImageField(upload_to='about_quality_trust', default="")


class HomeSRFP(models.Model):
    satisfied_clients = models.CharField(max_length=100, default="")
    resolution = models.CharField(max_length=100, default="")
    flight_time = models.CharField(max_length=100, default="")
    project_done = models.CharField(max_length=100, default="")


class VideoGallery(models.Model):
    video_link = models.CharField(max_length=200, default="")
    icon = models.ImageField(upload_to='Home/Video_Gallery', default="")


class WhatPeopleSay(models.Model):
    name = models.CharField(max_length=200, default="")
    designation = models.CharField(max_length=200, default="")
    say_something = models.TextField(default="")
    icon = models.ImageField(upload_to='Home/Testimonials', default="")


class OurPartner(models.Model):
    company_name = models.CharField(max_length=200, default="")
    description = models.TextField(default="")
    logo = models.ImageField(upload_to='Home/Partners', default="")


class OurTeam(models.Model):
    name = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=100, default="")
    phone = models.CharField(max_length=100, default="")
    experience = models.CharField(max_length=100, default="")
    designation = models.CharField(max_length=100, default="")
    socialmedia1 = models.CharField(max_length=100, default="")
    socialmedia2 = models.CharField(max_length=100, default="")
    socialmedia3 = models.CharField(max_length=100, default="")
    description = models.TextField(default="")
    profile = models.ImageField(upload_to='our_team', default="")


class ServicesTypes(models.Model):
    title = models.CharField(max_length=100, default="")
    Description = models.TextField(default="")
    quote = models.CharField(max_length=100, default="")
    quote_by = models.CharField(max_length=100, default="")
    type = models.CharField(max_length=100, choices=ServiceType, default="")
    highlight1 = models.CharField(max_length=100, default="")
    highlight2 = models.CharField(max_length=100, default="")
    highlight3 = models.CharField(max_length=100, default="")
    highlight4 = models.CharField(max_length=100, default="")
    highlight5 = models.CharField(max_length=100, default="")
    highlight6 = models.CharField(max_length=100, default="")
    icons = models.ImageField(upload_to='services', default="")


class Pricing(models.Model):
    category = models.CharField(max_length=255, choices=category, default="")
    price = models.CharField(max_length=255, default="")
    feature1 = models.CharField(max_length=255, default="")
    feature2 = models.CharField(max_length=255, default="")
    feature3 = models.CharField(max_length=255, default="")
    feature4 = models.CharField(max_length=255, default="")
    feature5 = models.CharField(max_length=255, default="")


class Gallery(models.Model):
    title = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=100, choices=category, default="")
    description = models.TextField(default="")
    image = models.ImageField(upload_to='Gallery', default="")


class SocialMedia(models.Model):
    email = models.EmailField(max_length=255, default="")
    skype = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=255, default="")
    github = models.CharField(max_length=255, default="")
    linkedin = models.CharField(max_length=255, default="")
    google_plus = models.CharField(max_length=255, default="")
    youtube = models.CharField(max_length=255, default="")
    facebook = models.CharField(max_length=255, default="")
    twitter = models.CharField(max_length=255, default="")


class userBlog(models.Model):
    sNo = models.AutoField(primary_key=True)
    title = models.TextField(default="")
    heading = models.TextField(default="")
    tags = models.TextField(default="")
    quote = models.TextField(default="")
    quote_by = models.TextField(default="")
    description = RichTextField(default="")
    Icon = models.ImageField(upload_to='Blog/Icons', default="")
    created_at = models.DateTimeField(default=django.utils.timezone.now())


class seoTags(models.Model):
    title = models.TextField(default="")
    page = models.TextField(default="")
    description = models.TextField(default="")
    tags = models.TextField(default="")
