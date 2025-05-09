# Generated by Django 5.1.6 on 2025-04-07 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_interior_seat_material_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interior',
            name='seat_material',
            field=models.CharField(blank=True, choices=[('leather', 'Кожаный'), ('velour', 'Велюр'), ('combined', 'Комбинированный'), ('cloth', 'Тряпичный'), ('other', 'Другое')], max_length=20, null=True, verbose_name='Материал сидений'),
        ),
    ]
