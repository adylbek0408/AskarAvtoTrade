from apps.common.views import BaseCarViewSet
from rest_framework import viewsets
from .models import Korea, ComparisonsKorea
from .serializers import KoreaSerializer, ComparisonsKoreaSerializer


class KoreaViewSet(BaseCarViewSet):
    serializer_class = KoreaSerializer
    queryset = Korea.objects.all()


class ComparisonsKoreaViewSet(viewsets.ModelViewSet):
    queryset = ComparisonsKorea.objects.all()
    serializer_class = ComparisonsKoreaSerializer
