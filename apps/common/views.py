from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.db.models import Prefetch
from .models import CarPhoto


# Базовый класс ViewSet для использования в приложениях
class BaseCarViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]

    def get_queryset(self):

        return self.queryset.select_related(
            'brand', 'model', 'color', 'body_type', 'manager',
            'interior', 'interior__interior_color', 'car_history'
        ).prefetch_related(
            Prefetch('photos', queryset=CarPhoto.objects.all())
        ).order_by('-auction_start_time')

