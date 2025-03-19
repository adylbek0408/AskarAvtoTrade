from rest_framework import serializers
from .models import Car, CarBrand, CarModel, Color, BodyType, Manager, Interior, CarHistory, CarPhoto


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ['id', 'name', 'logo']


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['id', 'name']


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name', 'hex_code']


class BodyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyType
        fields = ['id', 'name']


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id', 'full_name', 'phone_number', 'whatsapp_url']


class InteriorSerializer(serializers.ModelSerializer):
    interior_color = ColorSerializer()

    class Meta:
        model = Interior
        fields = ['id', 'steering_wheel', 'interior_color', 'seat_material']


class CarHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarHistory
        fields = ['id', 'carfax_status', 'damage_photos', 'vin_code']


class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPhoto
        fields = ['id', 'image', 'is_main']


class CarSerializer(serializers.ModelSerializer):
    brand = CarBrandSerializer()
    model = CarModelSerializer()
    color = ColorSerializer()
    body_type = BodyTypeSerializer()
    manager = ManagerSerializer()
    interior = InteriorSerializer(source='interior_set.first')
    car_history = CarHistorySerializer(source='carhistory_set.first')
    photos = CarPhotoSerializer(many=True, read_only=True)
    time_left = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = [
            'id', 'brand', 'model', 'year', 'mileage', 'engine_volume',
            'power', 'configuration', 'color', 'body_type', 'fuel_type',
            'transmission_type', 'start_price', 'end_price', 'manager',
            'auction_start_time', 'interior', 'car_history', 'photos', 'time_left'
        ]

    def get_time_left(self, obj):
        return obj.time_until_auction()
