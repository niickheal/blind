# Generated by Django 2.0.13 on 2020-01-12 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_attendence'),
    ]

    operations = [
        migrations.DeleteModel(
            name='attendence',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='feed_images',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='news_url',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='timestamp',
        ),
    ]