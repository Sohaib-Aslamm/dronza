# Generated by Django 4.0.3 on 2022-04-21 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=100)),
                ('subject', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=254)),
                ('message', models.TextField(default='')),
            ],
        ),
    ]
