from rest_framework import serializers
from .models import Korea, ComparisonsKorea
from ..common.serializers import BaseCarSerializer


class KoreaSerializer(BaseCarSerializer):
    class Meta:
        model = Korea
        fields = [
            'id', 'manager', 'brand', 'model', 'year', 'mileage', 'engine_volume',
            'power', 'configuration', 'color', 'body_type', 'fuel_type',
            'transmission_type', 'start_price', 'end_price', 'auction_start_time',
            'interior', 'car_history', 'photos', 'url', 'time_left'
        ]


class ComparisonsKoreaSerializer(serializers.ModelSerializer):
    korea_car = KoreaSerializer()

    class Meta:
        model = ComparisonsKorea
        fields = [
            'id', 'korea_car', 'comparisons',
        ]
