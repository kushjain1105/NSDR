# Generated by Django 4.1.2 on 2022-10-05 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]
