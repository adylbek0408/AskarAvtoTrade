# Generated by Django 5.1.6 on 2025-04-09 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('america', '0009_remove_america_body_type_america_body_type_choices'),
        ('common', '0004_remove_color_hex_code'),
        ('dubai', '0008_remove_dubai_body_type_dubai_body_type_choices'),
        ('korea', '0008_remove_korea_body_type_korea_body_type_choices'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BodyType',
        ),
    ]
