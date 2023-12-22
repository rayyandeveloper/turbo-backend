# Generated by Django 5.0 on 2023-12-22 16:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('key', models.CharField(editable=False, max_length=40, primary_key=True, serialize=False, verbose_name='Key')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auth_tokens', to='shop.shop', verbose_name='User')),
            ],
            options={
                'verbose_name': 'Token',
                'verbose_name_plural': 'Tokens',
            },
        ),
    ]
