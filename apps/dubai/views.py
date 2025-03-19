from apps.common.views import BaseCarViewSet
from .models import Dubai
from .serializers import DubaiSerializer


class DubaiViewSet(BaseCarViewSet):
    serializer_class = DubaiSerializer
    queryset = Dubai.objects.all()
