# Generated by Django 5.1.6 on 2025-03-19 14:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('america', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='america',
            name='auction_start_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время начала аукциона'),
        ),
    ]
