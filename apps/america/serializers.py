from rest_framework import serializers
from .models import America, ComparisonsAmerica
from apps.common.serializers import (
    CarBrandSerializer, CarModelSerializer, ColorSerializer,
    BodyTypeSerializer, InteriorSerializer, CarHistorySerializer,
    CarPhotoSerializer
)


class AmericaSerializer(serializers.ModelSerializer):
    brand = CarBrandSerializer()
    model = CarModelSerializer()
    color = ColorSerializer()
    body_type = BodyTypeSerializer()
    interior = InteriorSerializer()
    car_history = CarHistorySerializer()
    photos = CarPhotoSerializer(many=True)
    time_left = serializers.SerializerMethodField()

    class Meta:
        model = America
        fields = [
            'id', 'brand', 'model', 'year', 'mileage', 'engine_volume',
            'power', 'configuration', 'color', 'body_type', 'fuel_type',
            'transmission_type', 'start_price', 'end_price', 'auction_start_time',
            'interior', 'car_history', 'photos', 'url', 'time_left'
        ]

    def get_time_left(self, obj):
        return obj.time_until_auction()


class ComparisonsAmericaSerializer(serializers.ModelSerializer):
    america_car = AmericaSerializer()

    class Meta:
        model = ComparisonsAmerica
        fields = [
            'id', 'america_car', 'comparisons',
        ]
