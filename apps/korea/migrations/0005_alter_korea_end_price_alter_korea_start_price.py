# Generated by Django 5.1.6 on 2025-04-04 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korea', '0004_auto_20250403_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='korea',
            name='end_price',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Конечная цена'),
        ),
        migrations.AlterField(
            model_name='korea',
            name='start_price',
            field=models.PositiveIntegerField(db_index=True, verbose_name='Начальная цена'),
        ),
    ]
