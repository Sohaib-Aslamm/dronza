# Generated by Django 4.0.3 on 2022-04-09 17:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dronzaPanel', '0010_alter_userblog_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='category',
            new_name='category1',
        ),
        migrations.AlterField(
            model_name='userblog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 9, 17, 22, 49, 322239, tzinfo=utc)),
        ),
    ]
