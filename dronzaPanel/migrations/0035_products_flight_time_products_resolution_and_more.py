# Generated by Django 4.0.3 on 2022-04-19 11:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dronzaPanel', '0034_gallery_image_alter_userblog_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='flight_time',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='products',
            name='resolution',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userblog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 19, 11, 22, 3, 58911, tzinfo=utc)),
        ),
    ]
