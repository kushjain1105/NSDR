# Generated by Django 3.2.2 on 2022-10-21 07:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Research', '0003_auto_20221021_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 10, 21, 13, 20, 35, 722362)),
        ),
    ]
