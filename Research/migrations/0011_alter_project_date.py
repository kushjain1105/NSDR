# Generated by Django 4.1.2 on 2022-10-29 06:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Research', '0010_alter_project_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 10, 29, 11, 45, 30, 939330)),
        ),
    ]
