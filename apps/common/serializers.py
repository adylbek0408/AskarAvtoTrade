from rest_framework import serializers
from .models import Car, CarBrand, CarModel, Color, Manager, Interior, CarHistory, CarPhoto
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
                url = request.build_absolute_uri(obj.logo.url)
                url = url.replace(f'://{request.get_host()}', f'://{request.get_host().split(":")[0]}:800')
                return url
            return f'http://109.73.207.12:800{obj.logo.url}'
        return None


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['id', 'name']


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
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
                # Get the base URL with the correct port
                url = request.build_absolute_uri(obj.image.url)
                # Replace the default port with port 800
                url = url.replace(f'://{request.get_host()}', f'://{request.get_host().split(":")[0]}:800')
                return url
            # If no request available, construct URL manually
            return f'http://109.73.207.12:800{obj.image.url}'
        return None


class BaseCarSerializer(serializers.ModelSerializer):
    manager = ManagerSerializer()
    brand = CarBrandSerializer()
    model = CarModelSerializer()
    color = ColorSerializer()
    interior = serializers.SerializerMethodField()
    car_history = serializers.SerializerMethodField()
    photos = serializers.SerializerMethodField()
    time_left = serializers.SerializerMethodField()
    # drive_type = serializers.SerializerMethodField()
    # body_type_choices = serializers.SerializerMethodField()
    #
    # def get_drive_type(self, obj):
    #     return obj.get_drive_type_display()
    #
    # def get_body_type_choices(self, obj):
    #     return obj.get_body_type_display()

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

