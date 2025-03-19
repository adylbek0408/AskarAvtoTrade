from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.db.models import Prefetch
from .models import CarPhoto
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CarFilter


class BaseCarViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarFilter

    def get_queryset(self):
        queryset = self.queryset.select_related(
            'brand', 'model', 'color', 'body_type', 'manager'
        ).prefetch_related(
            Prefetch('photos', queryset=CarPhoto.objects.all())
        ).order_by('-auction_start_time')

        return queryset

