# Generated by Django 5.0 on 2023-12-23 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='device',
            field=models.CharField(default='None', max_length=256, verbose_name='Device'),
        ),
    ]
