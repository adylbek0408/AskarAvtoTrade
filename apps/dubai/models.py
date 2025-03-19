from django.db import models
from apps.common.models import Car


class Dubai(Car):
    url = models.URLField(verbose_name='Ссылка на машину')

    def __str__(self):
        return f"Дубай: {self.brand.name} {self.model.name} ({self.year})"

    class Meta:
        verbose_name = "Автомобиль из Дубая"
        verbose_name_plural = "Автомобили из Дубая"
