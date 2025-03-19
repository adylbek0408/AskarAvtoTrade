from rest_framework import serializers
from .models import Korea, ComparisonsKorea
from apps.common.serializers import (
    CarBrandSerializer, CarModelSerializer, ColorSerializer,
    BodyTypeSerializer, InteriorSerializer, CarHistorySerializer,
    CarPhotoSerializer
)


class KoreaSerializer(serializers.ModelSerializer):
    brand = CarBrandSerializer()
    model = CarModelSerializer()
    color = ColorSerializer()
    body_type = BodyTypeSerializer()
    interior = InteriorSerializer()
    car_history = CarHistorySerializer()
    photos = CarPhotoSerializer(many=True)
    time_left = serializers.SerializerMethodField()

    class Meta:
        model = Korea
        fields = [
            'id', 'brand', 'model', 'year', 'mileage', 'engine_volume',
            'power', 'configuration', 'color', 'body_type', 'fuel_type',
            'transmission_type', 'start_price', 'end_price', 'auction_start_time',
            'interior', 'car_history', 'photos', 'url', 'time_left'
        ]

    def get_time_left(self, obj):
        return obj.time_until_auction()


class ComparisonsKoreaSerializer(serializers.ModelSerializer):
    korea_car = KoreaSerializer()

    class Meta:
        model = ComparisonsKorea
        fields = [
            'id', 'korea_car', 'comparisons',
        ]
