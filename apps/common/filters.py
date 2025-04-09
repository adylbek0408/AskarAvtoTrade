# Complete filters.py
import django_filters
from .models import Car, BodyType


class CarFilter(django_filters.FilterSet):
    price_from = django_filters.NumberFilter(
        field_name='start_price',
        lookup_expr='gte',
        help_text="Минимальная стартовая цена"
    )
    price_to = django_filters.NumberFilter(
        field_name='start_price',
        lookup_expr='lte',
        help_text="Максимальная стартовая цена"
    )
    year = django_filters.RangeFilter(
        field_name='year',
        help_text="Диапазон год (например, year_min=2010&year_max=2020)"
    )
    mileage = django_filters.RangeFilter(
        field_name='mileage',
        help_text="Диапазон пробега в км"
    )
    transmission_type = django_filters.ChoiceFilter(
        choices=Car.TRANSMISSION_TYPE_CHOICES,
        help_text="Тип КПП"
    )
    fuel_type = django_filters.ChoiceFilter(
        choices=Car.FUEL_TYPE_CHOICES,
        help_text="Тип топлива"
    )
    body_type = django_filters.ModelChoiceFilter(
        field_name='body_type__name',
        queryset=BodyType.objects.all(),
        label="Кузов",
        help_text="Тип кузова"
    )

    drive_type = django_filters.ChoiceFilter(
        choices=Car.DRIVE_TYPE_CHOICES,
        help_text="Тип привода",
        label="Привод"
    )

    ordering = django_filters.OrderingFilter(
        fields=(
            ('start_price', 'price'),
            ('year', 'year'),
            ('mileage', 'mileage'),
            ('auction_start_time', 'auction_date')
        ),
        help_text="Поле для оформления заказа"
    )

    class Meta:
        model = Car
        fields = []
