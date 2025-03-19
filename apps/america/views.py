from apps.common.views import BaseCarViewSet
from .models import America
from .serializers import AmericaSerializer


class AmericaViewSet(BaseCarViewSet):
    serializer_class = AmericaSerializer
    queryset = America.objects.all()
