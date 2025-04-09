from django.db import models
from apps.common.models import Car


class Dubai(Car):
    url = models.URLField(
        verbose_name='Ссылка на машину',
        null=True,
        blank=True,
        default=''
    )

    @property
    def photos(self):
        return super().get_photos()

    def __str__(self):
        return f"Дубай: {self.brand.name} {self.model.name} ({self.year})"

    class Meta(Car.Meta):
        verbose_name = "Автомобиль из Дубая"
        verbose_name_plural = "Автомобили из Дубая"


class ComparisonsDubai(models.Model):
    dubai_car = models.ForeignKey(Dubai, on_delete=models.CASCADE, verbose_name='Дубай:', related_name='dubai_cars')
    comparisons = models.BooleanField(default=False, verbose_name='Сравнение')

    def __str__(self):
        return f"{self.comparisons} - {self.dubai_car}"

    class Meta:
        verbose_name = "Сравнение Дубай"
        verbose_name_plural = "Сравнение Дубай"


