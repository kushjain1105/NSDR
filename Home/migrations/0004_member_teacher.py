# Generated by Django 3.2.2 on 2022-10-14 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_alter_member_member_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='teacher',
            field=models.BooleanField(default=False),
        ),
    ]
