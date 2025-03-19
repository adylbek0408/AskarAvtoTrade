from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DubaiViewSet

app_name = 'dubai'

router = DefaultRouter()
router.register(r'cars', DubaiViewSet, basename='dubai-cars')

urlpatterns = [
    path('', include(router.urls)),
]
