# Generated by Django 5.1.6 on 2025-04-01 14:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('america', '0001_initial'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='america',
            name='body_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.bodytype', verbose_name='Тип кузова'),
        ),
        migrations.AddField(
            model_name='america',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.carbrand', verbose_name='Марка'),
        ),
        migrations.AddField(
            model_name='america',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.color', verbose_name='Цвет'),
        ),
        migrations.AddField(
            model_name='america',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.manager', verbose_name='Менеджер'),
        ),
        migrations.AddField(
            model_name='america',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.carmodel', verbose_name='Модель'),
        ),
        migrations.AddField(
            model_name='comparisonsamerica',
            name='america_car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='america_cars', to='america.america', verbose_name='Америка:'),
        ),
    ]
