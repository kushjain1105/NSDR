# Generated by Django 4.1.2 on 2022-10-20 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Script', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='nsdr_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='script',
            name='nsdrType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Script.nsdr_type'),
        ),
    ]
