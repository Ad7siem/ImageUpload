# Generated by Django 4.2.5 on 2023-10-03 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ImageUpdate', '0007_images_image_200px_images_image_400px'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image_200px',
            field=models.ImageField(blank=True, null=True, upload_to='images/200px/'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image_400px',
            field=models.ImageField(blank=True, null=True, upload_to='images/400px/'),
        ),
    ]
