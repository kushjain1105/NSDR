# Generated by Django 4.1.2 on 2022-11-01 06:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Research', '0016_alter_project_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 11, 1, 12, 7, 41, 692787)),
        ),
    ]