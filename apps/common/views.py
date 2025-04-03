from collections import defaultdict
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from django.contrib.contenttypes.models import ContentType
from .models import CarBrand, CarModel, CarPhoto, Manager
from .serializers import BaseCarSerializer, CarBrandSerializer, CarModelSerializer, ManagerSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CarFilter


class BaseCarViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BaseCarSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarFilter

    def get_queryset(self):
        model = self.queryset.model
        content_type = ContentType.objects.get_for_model(model)
        queryset = super().get_queryset().select_related(
            'brand', 'model', 'color', 'body_type', 'manager'
        )

        car_ids = queryset.values_list('id', flat=True)
        photos = CarPhoto.objects.filter(
            content_type=content_type,
            object_id__in=car_ids
        )

        photo_map = defaultdict(list)
        for photo in photos:
            photo_map[photo.object_id].append(photo)

        for car in queryset:
            car.prefetched_photos = photo_map.get(car.id, [])

        return queryset.order_by('-auction_start_time')


class CarBrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class CarModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CarModel.objects.all().select_related('brand')
    serializer_class = CarModelSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'brand': ['exact'],
        'brand__name': ['icontains'],
        'name': ['icontains']
    }

    def get_queryset(self):
        return super().get_queryset().order_by('brand__name', 'name')


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_fields = ['full_name', 'phone_number']

