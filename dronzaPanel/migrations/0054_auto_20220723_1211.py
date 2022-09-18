# Generated by Django 3.2.13 on 2022-07-23 12:11

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import dronzaPanel.models


class Migration(migrations.Migration):

    dependencies = [
        ('dronzaPanel', '0053_auto_20220703_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='amazonProduct',
            fields=[
                ('sNo', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=100)),
                ('cPrice', models.CharField(default='', max_length=100)),
                ('dPrice', models.CharField(default='', max_length=100)),
                ('brand', models.CharField(default='', max_length=100)),
                ('color', models.CharField(default='', max_length=100)),
                ('availability', models.CharField(choices=[('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock')], default='', max_length=100)),
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
        migrations.AlterField(
            model_name='userblog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 23, 12, 11, 57, 860449, tzinfo=utc)),
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
