from django.db import models
from apps.common.models import Car


class America(Car):
    url = models.URLField(verbose_name='Ссылка на машину')

    def __str__(self):
        return f"Америка: {self.brand.name} {self.model.name} ({self.year})"

    class Meta:
        verbose_name = "Автомобиль из Америки"
        verbose_name_plural = "Автомобили из Америки"
