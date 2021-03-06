# Generated by Django 2.0.13 on 2019-11-15 16:37

import app.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='feed_images',
            field=models.ImageField(blank=True, null=True, upload_to=app.models.upload_feed_image),
        ),
        migrations.AddField(
            model_name='feed',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
