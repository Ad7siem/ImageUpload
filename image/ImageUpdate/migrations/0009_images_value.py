# Generated by Django 4.2.5 on 2023-10-03 15:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ImageUpdate', '0008_alter_images_image_200px_alter_images_image_400px'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='value',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(300), django.core.validators.MaxValueValidator(30000)]),
        ),
    ]
