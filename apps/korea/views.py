from apps.common.views import BaseCarViewSet
from .models import Korea
from .serializers import KoreaSerializer


class KoreaViewSet(BaseCarViewSet):
    serializer_class = KoreaSerializer
    queryset = Korea.objects.all()
