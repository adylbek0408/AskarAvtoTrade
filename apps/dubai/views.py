from apps.common.views import BaseCarViewSet
from rest_framework import viewsets
from .models import Dubai, ComparisonsDubai
from .serializers import DubaiSerializer, ComparisonsDubaiSerializer


class DubaiViewSet(BaseCarViewSet):
    serializer_class = DubaiSerializer
    queryset = Dubai.objects.all()


class ComparisonsDubaiViewSet(viewsets.ModelViewSet):
    queryset = ComparisonsDubai.objects.all()
    serializer_class = ComparisonsDubaiSerializer
