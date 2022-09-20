# Generated by Django 4.1 on 2022-09-20 11:41

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
import dronzaPanel.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutTitlePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('description', models.TextField(default='')),
                ('feature1', models.TextField(default='')),
                ('feature2', models.TextField(default='')),
                ('feature3', models.TextField(default='')),
                ('image', models.ImageField(default='', upload_to='about_title_post')),
            ],
        ),
        migrations.CreateModel(
            name='amazonProduct',
            fields=[
                ('sNo', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=255)),
                ('cPrice', models.CharField(default='', max_length=100)),
                ('dPrice', models.CharField(default='', max_length=100)),
                ('category', models.CharField(choices=[('Metal', 'Metal'), ('Fabric', 'Fabric'), ('Wireless', 'Wireless'), ('Plastic', 'Plastic'), ('Titanium', 'Titanium'), ('Featured', 'Featured'), ('Other', 'Other')], default='', max_length=100)),
                ('brand', models.CharField(default='', max_length=100)),
                ('color', models.CharField(default='', max_length=100)),
                ('availability', models.CharField(choices=[('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock')], default='', max_length=100)),
                ('featured', models.CharField(choices=[('Featured', 'Featured'), ('Not_Featured', 'Not_Featured')], default='', max_length=100)),
                ('itemWeight', models.CharField(default='', max_length=100)),
                ('controlType', models.CharField(default='', max_length=100)),
                ('remoteControl', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='', max_length=100)),
                ('batteryCell', models.CharField(default='', max_length=100)),
                ('Rechargeable', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='', max_length=100)),
                ('flight_time', models.CharField(default='', max_length=100)),
                ('camera', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='')),
                ('buyLink', models.CharField(default='', max_length=255)),
                ('mainIcon', models.FileField(default='', upload_to='AmazonProducts/MainIcon')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('category', models.CharField(choices=[('Nature', 'Nature'), ('Urbanistic', 'Urbanistic'), ('Landscape', 'Landscape'), ('Sports', 'Sports'), ('Shooting', 'Shooting'), ('Traveling', 'Traveling')], default='', max_length=100)),
                ('description', models.TextField(default='')),
                ('image', models.ImageField(default='', upload_to='Gallery')),
            ],
        ),
        migrations.CreateModel(
            name='HomeAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('description', models.TextField(default='')),
                ('feature1', models.CharField(default='', max_length=100)),
                ('feature2', models.CharField(default='', max_length=100)),
                ('feature3', models.CharField(default='', max_length=100)),
                ('icon', models.ImageField(default='', upload_to='Home_About')),
            ],
        ),
        migrations.CreateModel(
            name='HomeHIW',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('description', models.TextField(default='')),
                ('image', models.ImageField(default='', upload_to='Home_HowITWORK')),
            ],
        ),
        migrations.CreateModel(
            name='HomeHTU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('description', models.TextField(default='')),
                ('icon', models.ImageField(default='', upload_to='Home_HowToUse')),
            ],
        ),
        migrations.CreateModel(
            name='HomeSRFP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('satisfied_clients', models.CharField(default='', max_length=100)),
                ('resolution', models.CharField(default='', max_length=100)),
                ('flight_time', models.CharField(default='', max_length=100)),
                ('project_done', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MainSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('header', models.TextField(default='')),
                ('description', models.TextField(default='')),
                ('price', models.TextField(default='')),
                ('image', models.ImageField(default='', upload_to='Home_Main_Slider')),
                ('backImage', models.ImageField(default='', upload_to='slide_back_Image')),
            ],
        ),
        migrations.CreateModel(
            name='OurPartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='', max_length=200)),
                ('description', models.TextField(default='')),
                ('logo', models.ImageField(default='', upload_to='Home/Partners')),
            ],
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('designation', models.CharField(default='', max_length=100)),
                ('socialmedia1', models.CharField(default='', max_length=100)),
                ('socialmedia2', models.CharField(default='', max_length=100)),
                ('socialmedia3', models.CharField(default='', max_length=100)),
                ('profile', models.ImageField(default='', upload_to='our_team')),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Nature', 'Nature'), ('Urbanistic', 'Urbanistic'), ('Landscape', 'Landscape'), ('Sports', 'Sports'), ('Shooting', 'Shooting'), ('Traveling', 'Traveling')], default='', max_length=255)),
                ('price', models.CharField(default='', max_length=255)),
                ('feature1', models.CharField(default='', max_length=255)),
                ('feature2', models.CharField(default='', max_length=255)),
                ('feature3', models.CharField(default='', max_length=255)),
                ('feature4', models.CharField(default='', max_length=255)),
                ('feature5', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('cPrice', models.CharField(default='', max_length=100)),
                ('price', models.CharField(default='', max_length=100)),
                ('availability', models.CharField(choices=[('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock')], default='', max_length=100)),
                ('resolution', models.CharField(default='', max_length=100)),
                ('flight_time', models.CharField(default='', max_length=100)),
                ('color', models.CharField(default='', max_length=100)),
                ('featured', models.CharField(choices=[('Featured', 'Featured'), ('Not_Featured', 'Not_Featured')], default='', max_length=100)),
                ('category', models.CharField(choices=[('Metal', 'Metal'), ('Fabric', 'Fabric'), ('Wireless', 'Wireless'), ('Plastic', 'Plastic'), ('Titanium', 'Titanium'), ('Featured', 'Featured'), ('Other', 'Other')], default='', max_length=100)),
                ('label1', models.CharField(default='', max_length=100)),
                ('label2', models.CharField(default='', max_length=100)),
                ('label3', models.CharField(default='', max_length=100)),
                ('label4', models.CharField(default='', max_length=100)),
                ('label5', models.CharField(default='', max_length=100)),
                ('label6', models.CharField(default='', max_length=100)),
                ('input1', models.CharField(default='', max_length=100)),
                ('input2', models.CharField(default='', max_length=100)),
                ('input3', models.CharField(default='', max_length=100)),
                ('input4', models.CharField(default='', max_length=100)),
                ('input5', models.CharField(default='', max_length=100)),
                ('input6', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='')),
                ('image', models.FileField(default='', upload_to='DronzaProducts/MainIcon')),
            ],
        ),
        migrations.CreateModel(
            name='QualityTrust',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('Description', models.TextField(default='')),
                ('icon', models.ImageField(default='', upload_to='about_quality_trust')),
            ],
        ),
        migrations.CreateModel(
            name='ServicesTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('Description', models.TextField(default='')),
                ('quote', models.CharField(default='', max_length=100)),
                ('quote_by', models.CharField(default='', max_length=100)),
                ('type', models.CharField(choices=[('RegularService', 'RegularService'), ('MainService', 'MainService')], default='', max_length=100)),
                ('highlight1', models.CharField(default='', max_length=100)),
                ('highlight2', models.CharField(default='', max_length=100)),
                ('highlight3', models.CharField(default='', max_length=100)),
                ('highlight4', models.CharField(default='', max_length=100)),
                ('highlight5', models.CharField(default='', max_length=100)),
                ('highlight6', models.CharField(default='', max_length=100)),
                ('icons', models.ImageField(default='', upload_to='services')),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='', max_length=255)),
                ('skype', models.CharField(default='', max_length=255)),
                ('phone', models.CharField(default='', max_length=255)),
                ('github', models.CharField(default='', max_length=255)),
                ('linkedin', models.CharField(default='', max_length=255)),
                ('google_plus', models.CharField(default='', max_length=255)),
                ('youtube', models.CharField(default='', max_length=255)),
                ('facebook', models.CharField(default='', max_length=255)),
                ('twitter', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='userBlog',
            fields=[
                ('sNo', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=255)),
                ('heading', models.CharField(default='', max_length=255)),
                ('tags', models.CharField(default='', max_length=255)),
                ('quote', models.CharField(default='', max_length=255)),
                ('quote_by', models.CharField(default='', max_length=255)),
                ('description', ckeditor.fields.RichTextField(default='')),
                ('Icon', models.ImageField(default='', upload_to='Blog/Icons')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 9, 20, 11, 41, 34, 434711, tzinfo=datetime.timezone.utc))),
            ],
        ),
        migrations.CreateModel(
            name='VideoGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_link', models.CharField(default='', max_length=200)),
                ('icon', models.ImageField(default='', upload_to='Home/Video_Gallery')),
            ],
        ),
        migrations.CreateModel(
            name='WhatPeopleSay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('designation', models.CharField(default='', max_length=200)),
                ('say_something', models.TextField(default='')),
                ('icon', models.ImageField(default='', upload_to='Home/Testimonials')),
            ],
        ),
        migrations.CreateModel(
            name='productImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to=dronzaPanel.models.productImages.upload_design_to)),
                ('Product_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dronzaPanel.products')),
            ],
        ),
        migrations.CreateModel(
            name='amazonProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to=dronzaPanel.models.amazonProductImages.upload_design_to)),
                ('Product_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dronzaPanel.amazonproduct')),
            ],
        ),
    ]