# Generated by Django 4.2.5 on 2023-10-03 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ImageUpdate', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='userprofile',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='ImageUpdate.userprofile'),
            preserve_default=False,
        ),
    ]
