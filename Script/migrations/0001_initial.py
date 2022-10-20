# Generated by Django 4.1.2 on 2022-10-20 06:15

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Audio')),
                ('name', models.CharField(max_length=250)),
                ('duration', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
