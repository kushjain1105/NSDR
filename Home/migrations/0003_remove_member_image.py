# Generated by Django 3.2.2 on 2022-10-04 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_member_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='image',
        ),
    ]