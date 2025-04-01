from django.db import models
from apps.common.models import Car


class Korea(Car):
    url = models.URLField(verbose_name='Ссылка на машину', null=True, blank=True, default='')

    def __str__(self):
        return f"Корея: {self.brand.name} {self.model.name} ({self.year})"

    class Meta:
        verbose_name = "Автомобиль из Кореи"
        verbose_name_plural = "Автомобили из Кореи"


class ComparisonsKorea(models.Model):
    korea_car = models.ForeignKey(Korea, on_delete=models.CASCADE, verbose_name='Корея:', related_name='korea_cars')
    comparisons = models.BooleanField(default=False, verbose_name='Сравнение')

    def __str__(self):
        return f"{self.comparisons} - {self.korea_car}"

    class Meta:
        verbose_name = "Сравнение Корея"
        verbose_name_plural = "Сравнение Корея"
