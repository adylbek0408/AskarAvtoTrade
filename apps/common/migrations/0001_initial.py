# Generated by Django 5.1.6 on 2025-04-01 14:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BodyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Тип кузова')),
            ],
            options={
                'verbose_name': 'Тип кузова',
                'verbose_name_plural': 'Типы кузовов',
            },
        ),
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Марка')),
                ('logo', models.ImageField(upload_to='brands/logos/', verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Марка автомобиля',
                'verbose_name_plural': 'Марки автомобилей',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название цвета')),
                ('hex_code', models.CharField(blank=True, max_length=7, null=True, verbose_name='Код цвета (HEX)')),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвета',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('whatsapp_url', models.URLField(verbose_name='Ссылка на WhatsApp')),
            ],
            options={
                'verbose_name': 'Менеджер',
                'verbose_name_plural': 'Менеджеры',
            },
        ),
        migrations.CreateModel(
            name='CarHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('carfax_status', models.CharField(choices=[('clean', 'Чистый'), ('dirty', 'Не чистый')], max_length=10, verbose_name='Статус Carfax')),
                ('vin_code', models.CharField(max_length=17, verbose_name='VIN код')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'История автомобиля',
                'verbose_name_plural': 'Истории автомобилей',
            },
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Модель')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='common.carbrand', verbose_name='Марка')),
            ],
            options={
                'verbose_name': 'Модель автомобиля',
                'verbose_name_plural': 'Модели автомобилей',
            },
        ),
        migrations.CreateModel(
            name='CarPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cars/photos/', verbose_name='Фото')),
                ('is_main', models.BooleanField(default=False, verbose_name='Основное фото')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Фото автомобиля',
                'verbose_name_plural': 'Фото автомобилей',
            },
        ),
        migrations.CreateModel(
            name='Interior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('steering_wheel', models.CharField(choices=[('right', 'Правый'), ('left', 'Левый')], max_length=20, verbose_name='Руль')),
                ('seat_material', models.CharField(choices=[('leather', 'Кожаный'), ('velour', 'Велюр'), ('combined', 'Комбинированный'), ('cloth', 'Тряпичный')], max_length=20, verbose_name='Материал сидений')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('interior_color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='interiors', to='common.color', verbose_name='Цвет салона')),
            ],
            options={
                'verbose_name': 'Интерьер',
                'verbose_name_plural': 'Интерьеры',
            },
        ),
    ]
