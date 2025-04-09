import django_filters
from django import forms
from django.db.models import Q
from .models import Car, BodyType, CarBrand


class CommaSeparatedModelMultipleChoiceFilter(django_filters.ModelMultipleChoiceFilter):
    def filter(self, qs, value):
        if not value:
            return qs

        return super().filter(qs, value)

    def get_filter_value(self, value):
        if isinstance(value, str):
            return value.split(',')
        return value


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

    transmission_type = django_filters.MultipleChoiceFilter(
        choices=Car.TRANSMISSION_TYPE_CHOICES,
        help_text="Тип КПП (например, manual,automatic)",
        widget=forms.CheckboxSelectMultiple,
    )

    fuel_type = django_filters.MultipleChoiceFilter(
        choices=Car.FUEL_TYPE_CHOICES,
        help_text="Тип топлива (например, petrol,diesel)",
        widget=forms.CheckboxSelectMultiple,
    )

    drive_type = django_filters.MultipleChoiceFilter(
        choices=Car.DRIVE_TYPE_CHOICES,
        help_text="Тип привода (например, fwd,rwd)",
        widget=forms.CheckboxSelectMultiple,
    )

    body_type = CommaSeparatedModelMultipleChoiceFilter(
        field_name='body_type__name',
        to_field_name='name',
        queryset=BodyType.objects.all(),
        help_text="Тип кузова (например, sedan,hatchback)",
        widget=forms.CheckboxSelectMultiple,
    )

    brand = CommaSeparatedModelMultipleChoiceFilter(
        field_name='brand__name',
        to_field_name='name',
        queryset=CarBrand.objects.all(),
        help_text="Марка автомобиля (например, BMW,Audi)",
        widget=forms.CheckboxSelectMultiple,
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
