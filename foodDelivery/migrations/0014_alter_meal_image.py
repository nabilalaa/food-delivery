# Generated by Django 5.1 on 2024-09-24 13:09

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodDelivery', '0013_alter_meal_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='food'),
        ),
    ]
