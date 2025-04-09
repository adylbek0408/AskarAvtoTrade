import django_filters
from django import forms
from .models import Car, BodyType, CarBrand


class CarFilter(django_filters.FilterSet):
    # Existing filters
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

    # Updated filters for multiple selection
    transmission_type = django_filters.MultipleChoiceFilter(
        choices=Car.TRANSMISSION_TYPE_CHOICES,
        help_text="Тип КПП",
        widget=forms.CheckboxSelectMultiple
    )
    fuel_type = django_filters.MultipleChoiceFilter(
        choices=Car.FUEL_TYPE_CHOICES,
        help_text="Тип топлива",
        widget=forms.CheckboxSelectMultiple
    )
    drive_type = django_filters.MultipleChoiceFilter(
        choices=Car.DRIVE_TYPE_CHOICES,
        help_text="Тип привода",
        widget=forms.CheckboxSelectMultiple
    )
    body_type = django_filters.ModelMultipleChoiceFilter(
        queryset=BodyType.objects.all(),
        help_text="Тип кузова",
        widget=forms.CheckboxSelectMultiple
    )

    # New brand filter
    brand = django_filters.ModelMultipleChoiceFilter(
        field_name='brand',
        queryset=CarBrand.objects.all(),
        help_text="Марка автомобиля",
        widget=forms.CheckboxSelectMultiple
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
