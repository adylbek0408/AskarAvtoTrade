# Generated by Django 5.1.6 on 2025-04-04 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interior',
            name='seat_material',
            field=models.CharField(choices=[('leather', 'Кожаный'), ('velour', 'Велюр'), ('combined', 'Комбинированный'), ('cloth', 'Тряпичный'), ('other', 'Другое')], max_length=20, verbose_name='Материал сидений'),
        ),
        migrations.AlterField(
            model_name='interior',
            name='steering_wheel',
            field=models.CharField(choices=[('right', 'Правый'), ('left', 'Левый'), ('center', 'Центральный')], max_length=20, verbose_name='Руль'),
        ),
        migrations.AddIndex(
            model_name='carphoto',
            index=models.Index(fields=['content_type', 'object_id'], name='common_carp_content_c78a1b_idx'),
        ),
    ]
