from rest_framework import serializers
from .models import Dubai, ComparisonsDubai
from ..common.serializers import BaseCarSerializer


class DubaiSerializer(BaseCarSerializer):
    class Meta:
        model = Dubai
        fields = [
            'id', 'manager', 'brand', 'model', 'year', 'mileage', 'engine_volume',
            'power', 'configuration', 'color', 'body_type', 'fuel_type',
            'transmission_type', 'start_price', 'end_price', 'auction_start_time',
            'interior', 'car_history', 'photos', 'url', 'time_left'
        ]


class ComparisonsDubaiSerializer(serializers.ModelSerializer):
    dubai_car = DubaiSerializer()

    class Meta:
        model = ComparisonsDubai
        fields = [
            'id', 'dubai_car', 'comparisons',
        ]
