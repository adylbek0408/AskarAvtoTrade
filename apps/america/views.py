from apps.common.views import BaseCarViewSet
from .models import America, ComparisonsAmerica
from .serializers import AmericaSerializer, ComparisonsAmericaSerializer
from rest_framework import viewsets


class AmericaViewSet(BaseCarViewSet):
    serializer_class = AmericaSerializer
    queryset = America.objects.all()


class ComparisonsAmericaViewSet(viewsets.ModelViewSet):
    queryset = ComparisonsAmerica.objects.all()
    serializer_class = ComparisonsAmericaSerializer
