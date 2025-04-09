from rest_framework import serializers
from .models import America, ComparisonsAmerica
from ..common.serializers import BaseCarSerializer


class AmericaSerializer(BaseCarSerializer):
    class Meta:
        model = America
        fields = [
            'id', 'manager', 'brand', 'model', 'year', 'mileage', 'engine_volume',
            'power', 'configuration', 'color', 'body_type', 'fuel_type',
            'transmission_type', 'drive_type', 'start_price', 'end_price', 'auction_start_time',
            'interior', 'car_history', 'photos', 'url', 'time_left'
        ]


class ComparisonsAmericaSerializer(serializers.ModelSerializer):
    america_car = AmericaSerializer()

    class Meta:
        model = ComparisonsAmerica
        fields = [
            'id', 'america_car', 'comparisons',
        ]
