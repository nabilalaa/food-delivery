# Generated by Django 5.1 on 2024-09-24 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodDelivery', '0006_alter_meal_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='image',
            field=models.ImageField(blank=True, upload_to='foods/'),
        ),
    ]
