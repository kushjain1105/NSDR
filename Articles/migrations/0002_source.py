# Generated by Django 3.2.2 on 2022-10-20 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('sourceURL', models.URLField()),
                ('articles', models.ManyToManyField(blank=True, related_name='sources', to='Articles.Article')),
            ],
        ),
    ]
