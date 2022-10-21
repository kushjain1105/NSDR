# Generated by Django 3.2.2 on 2022-10-21 11:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Research', '0006_alter_project_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='imageURL',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 10, 21, 16, 32, 58, 368630)),
        ),
    ]
