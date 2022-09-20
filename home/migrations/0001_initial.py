# Generated by Django 4.1 on 2022-09-20 11:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dronzaPanel', '0001_initial'),
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
        migrations.CreateModel(
            name='hello',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yourName', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=254)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Place_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(default='', max_length=100)),
                ('user_id', models.CharField(default='', max_length=100)),
                ('p_price', models.CharField(default='', max_length=100)),
                ('p_quantity', models.CharField(default='', max_length=100)),
                ('p_total', models.CharField(default='', max_length=100)),
                ('p_grand_total', models.CharField(default='', max_length=100)),
                ('c_name', models.CharField(default='', max_length=100)),
                ('c_email', models.CharField(default='', max_length=100)),
                ('c_phone', models.CharField(default='', max_length=100)),
                ('c_city', models.CharField(default='', max_length=100)),
                ('c_zip', models.CharField(default='', max_length=100)),
                ('c_country', models.CharField(default='', max_length=100)),
                ('c_address1', models.CharField(default='', max_length=100)),
                ('c_address2', models.CharField(default='', max_length=100)),
                ('status', models.CharField(default='', max_length=100)),
                ('order_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='sellYourDrone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('user_id', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=100)),
                ('pPhone', models.EmailField(default='', max_length=100)),
                ('sPhone', models.EmailField(default='', max_length=100)),
                ('location', models.EmailField(default='', max_length=255)),
                ('title', models.CharField(default='', max_length=255)),
                ('price', models.CharField(default='', max_length=100)),
                ('camera', models.CharField(default='', max_length=100)),
                ('flight_time', models.CharField(default='', max_length=100)),
                ('color', models.CharField(default='', max_length=100)),
                ('condition', models.CharField(default='', max_length=100)),
                ('category', models.CharField(default='', max_length=100)),
                ('label1', models.CharField(default='N/A', max_length=100, null=True)),
                ('label2', models.CharField(default='N/A', max_length=100, null=True)),
                ('label3', models.CharField(default='N/A', max_length=100, null=True)),
                ('label4', models.CharField(default='N/A', max_length=100, null=True)),
                ('input1', models.CharField(default='N/A', max_length=100, null=True)),
                ('input2', models.CharField(default='N/A', max_length=100, null=True)),
                ('input3', models.CharField(default='N/A', max_length=100, null=True)),
                ('input4', models.CharField(default='N/A', max_length=100, null=True)),
                ('description', models.TextField(default='')),
                ('thumbnail', models.FileField(default='', upload_to='sellYourDrone/thumbnail')),
            ],
        ),
        migrations.CreateModel(
            name='sellYourDroneImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to=home.models.sellYourDroneImages.upload_design_to)),
                ('Product_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.sellyourdrone')),
            ],
        ),
        migrations.CreateModel(
            name='productReview',
            fields=[
                ('sNo', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('review', models.TextField(default='')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.productreview')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dronzaPanel.amazonproduct')),
            ],
        ),
        migrations.CreateModel(
            name='blog_Review',
            fields=[
                ('sNo', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('comment', models.TextField(default='')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.blog_review')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dronzaPanel.userblog')),
            ],
        ),
    ]