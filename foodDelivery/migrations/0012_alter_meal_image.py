# Generated by Django 5.1 on 2024-09-24 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodDelivery', '0011_alter_meal_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='image',
            field=models.ImageField(blank=True, upload_to='food'),
        ),
    ]
