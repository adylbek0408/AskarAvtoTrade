from rest_framework import serializers
from .models import Car, CarBrand, CarModel, Color, BodyType, Manager, Interior, CarHistory, CarPhoto
from django.contrib.contenttypes.models import ContentType
from django.conf import settings


class CarBrandSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()

    class Meta:
        model = CarBrand
        fields = ['id', 'name', 'logo']

    def get_logo(self, obj):
        if obj.logo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.logo.url)
            return obj.logo.url
        return None


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
        fields = ['id', 'carfax_status', 'vin_code']


class CarPhotoSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = CarPhoto
        fields = ['id', 'image', 'is_main']

    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None


class BaseCarSerializer(serializers.ModelSerializer):
    manager = ManagerSerializer()
    brand = CarBrandSerializer()
    model = CarModelSerializer()
    color = ColorSerializer()
    body_type = BodyTypeSerializer()
    interior = serializers.SerializerMethodField()
    car_history = serializers.SerializerMethodField()
    photos = serializers.SerializerMethodField()
    time_left = serializers.SerializerMethodField()

    def get_interior(self, obj):
        interior = Interior.objects.filter(
            content_type=ContentType.objects.get_for_model(obj),
            object_id=obj.id
        ).first()
        if interior:
            return InteriorSerializer(interior).data
        return None

    def get_car_history(self, obj):
        history = CarHistory.objects.filter(
            content_type=ContentType.objects.get_for_model(obj),
            object_id=obj.id
        ).first()
        if history:
            return CarHistorySerializer(history).data
        return None

    def get_photos(self, obj):
        photos = getattr(obj, 'prefetched_photos', None)
        if not photos:
            photos = obj.get_photos()
        return CarPhotoSerializer(photos, many=True, context=self.context).data

    def get_time_left(self, obj):
        return obj.time_until_auction()

