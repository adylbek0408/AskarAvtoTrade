from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KoreaViewSet

app_name = 'korea'

router = DefaultRouter()
router.register(r'cars', KoreaViewSet, basename='korea-cars')

urlpatterns = [
    path('', include(router.urls)),
]
