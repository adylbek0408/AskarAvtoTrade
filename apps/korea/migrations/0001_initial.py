# Generated by Django 5.1.6 on 2025-03-22 12:27

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Korea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField(db_index=True, verbose_name='Год выпуска')),
                ('mileage', models.PositiveIntegerField(db_index=True, verbose_name='Пробег (км)')),
                ('engine_volume', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Объем двигателя (л)')),
                ('power', models.PositiveIntegerField(verbose_name='Мощность (л.с.)')),
                ('configuration', models.CharField(max_length=255, verbose_name='Комплектация')),
                ('fuel_type', models.CharField(choices=[('petrol', 'Бензин'), ('diesel', 'Дизель'), ('hybrid', 'Гибрид'), ('electric', 'Электрический'), ('hydrogen', 'Водород')], max_length=20, verbose_name='Тип топлива')),
                ('transmission_type', models.CharField(choices=[('manual', 'Механическая'), ('automatic', 'Автоматическая'), ('robot', 'Роботизированная'), ('variator', 'Вариатор'), ('dsg', 'DSG (Робот с двойным сцеплением)')], max_length=20, verbose_name='Тип КПП')),
                ('start_price', models.DecimalField(db_index=True, decimal_places=2, max_digits=12, verbose_name='Начальная цена')),
                ('end_price', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Конечная цена')),
                ('auction_start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время начала аукциона')),
                ('url', models.URLField(verbose_name='Ссылка на машину')),
                ('body_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.bodytype', verbose_name='Тип кузова')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.carbrand', verbose_name='Марка')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.color', verbose_name='Цвет')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.manager', verbose_name='Менеджер')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.carmodel', verbose_name='Модель')),
            ],
            options={
                'verbose_name': 'Автомобиль из Кореи',
                'verbose_name_plural': 'Автомобили из Кореи',
            },
        ),
        migrations.CreateModel(
            name='ComparisonsKorea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comparisons', models.BooleanField(default=False, verbose_name='Сравнение')),
                ('korea_car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='korea_cars', to='korea.korea', verbose_name='Дубай:')),
            ],
            options={
                'verbose_name': 'Сравнение Корея',
                'verbose_name_plural': 'Сравнение Корея',
            },
        ),
    ]
