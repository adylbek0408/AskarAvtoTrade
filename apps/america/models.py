from django.db import models
from apps.common.models import Car


class America(Car):
    url = models.URLField(verbose_name='Ссылка на машину', null=True, blank=True)

    def __str__(self):
        return f"Америка: {self.brand.name} {self.model.name} ({self.year})"

    class Meta:
        verbose_name = "Автомобиль из Америки"
        verbose_name_plural = "Автомобили из Америки"


class ComparisonsAmerica(models.Model):
    america_car = models.ForeignKey(America, on_delete=models.CASCADE, verbose_name='Америка:',
                                    related_name='america_cars')
    comparisons = models.BooleanField(default=False, verbose_name='Сравнение')

    def __str__(self):
        return f"{self.comparisons} - {self.america_car}"

    class Meta:
        verbose_name = "Сравнение Америка"
        verbose_name_plural = "Сравнение Америка"
       