# Generated by Django 5.0 on 2023-12-26 03:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_moneyhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='moneyhistory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
