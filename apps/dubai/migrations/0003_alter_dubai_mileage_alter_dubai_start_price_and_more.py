# Generated by Django 5.1.6 on 2025-03-19 16:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dubai', '0002_alter_dubai_auction_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dubai',
            name='mileage',
            field=models.PositiveIntegerField(db_index=True, verbose_name='Пробег (км)'),
        ),
        migrations.AlterField(
            model_name='dubai',
            name='start_price',
            field=models.DecimalField(db_index=True, decimal_places=2, max_digits=12, verbose_name='Начальная цена'),
        ),
        migrations.AlterField(
            model_name='dubai',
            name='year',
            field=models.PositiveIntegerField(db_index=True, verbose_name='Год выпуска'),
        ),
        migrations.CreateModel(
            name='ComparisonsDubai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comparisons', models.BooleanField(default=False, verbose_name='Сравнение')),
                ('dubai_car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dubai_cars', to='dubai.dubai', verbose_name='Дубай:')),
            ],
            options={
                'verbose_name': 'Сравнение Дубай',
                'verbose_name_plural': 'Сравнение Дубай',
            },
        ),
    ]
