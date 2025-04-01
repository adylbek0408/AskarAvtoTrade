from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.db.models import Prefetch
from .models import CarBrand, CarModel
from .serializers import BaseCarSerializer, CarBrandSerializer, CarModelSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CarFilter


class BaseCarViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BaseCarSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarFilter

    def get_queryset(self):
        # Переопределите этот метод в дочерних классах
        queryset = super().get_queryset()
        return queryset.select_related(
            'brand', 'model', 'color', 'body_type', 'manager'
        ).order_by('-auction_start_time')


class CarBrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


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
