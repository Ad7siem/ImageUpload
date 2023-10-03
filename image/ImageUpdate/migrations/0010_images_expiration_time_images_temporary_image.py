# Generated by Django 4.2.5 on 2023-10-03 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ImageUpdate', '0009_images_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='expiration_time',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='images',
            name='temporary_image',
            field=models.ImageField(blank=True, null=True, upload_to='temporary_images'),
        ),
    ]
