# Generated by Django 4.1.2 on 2022-10-05 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_school_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]