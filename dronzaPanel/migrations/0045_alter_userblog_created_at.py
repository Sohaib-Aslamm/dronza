# Generated by Django 4.0.3 on 2022-04-26 11:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dronzaPanel', '0044_alter_userblog_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userblog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 26, 11, 3, 58, 659667, tzinfo=utc)),
        ),
    ]
