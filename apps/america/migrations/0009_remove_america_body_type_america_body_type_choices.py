# Generated by Django 5.1.6 on 2025-04-09 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('america', '0008_america_drive_type_alter_america_engine_volume_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='america',
            name='body_type',
        ),
        migrations.AddField(
            model_name='america',
            name='body_type_choices',
            field=models.CharField(choices=[('sedan', 'Седан'), ('wagon', 'Универсал'), ('crossover', 'Кроссовер'), ('hatchback', 'Хэтчбек'), ('coupe', 'Купе'), ('convertible', 'Кабриолет'), ('liftback', 'Лифтбек'), ('pickup', 'Пикап'), ('minivan', 'Минивэн'), ('van', 'Фургон'), ('roadster', 'Родстер'), ('targa', 'Тарга'), ('limousine', 'Лимузин'), ('microvan', 'Микровэн'), ('suv', 'Внедорожник'), ('other', 'Другое')], default=1, max_length=30, verbose_name='Тип кузова'),
            preserve_default=False,
        ),
    ]
