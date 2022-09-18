# Generated by Django 3.2.13 on 2022-08-07 12:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dronzaPanel', '0061_auto_20220807_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazonproduct',
            name='category',
            field=models.CharField(choices=[('Metal', 'Metal'), ('Fabric', 'Fabric'), ('Wireless', 'Wireless'), ('Plastic', 'Plastic'), ('Titanium', 'Titanium'), ('Featured', 'Featured'), ('Other', 'Other')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('Metal', 'Metal'), ('Fabric', 'Fabric'), ('Wireless', 'Wireless'), ('Plastic', 'Plastic'), ('Titanium', 'Titanium'), ('Featured', 'Featured'), ('Other', 'Other')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userblog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 7, 12, 32, 49, 278284, tzinfo=utc)),
        ),
    ]
