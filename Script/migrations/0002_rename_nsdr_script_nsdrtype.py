# Generated by Django 4.1.2 on 2022-10-15 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Script', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='script',
            old_name='nsdr',
            new_name='nsdrType',
        ),
    ]