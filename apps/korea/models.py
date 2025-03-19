from django.db import models
from apps.common.models import Car


class Korea(Car):
    url = models.URLField(verbose_name='Ссылка на машину')

    def __str__(self):
        return f"Корея: {self.brand.name} {self.model.name} ({self.year})"

    class Meta:
        verbose_name = "Автомобиль из Кореи"
        verbose_name_plural = "Автомобили из Кореи"

