# Generated by Django 4.1.2 on 2022-10-05 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_school_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
