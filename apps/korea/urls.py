from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KoreaViewSet, ComparisonsKoreaViewSet

app_name = 'korea'

router = DefaultRouter()
router.register(r'cars', KoreaViewSet, basename='korea-cars')
router.register(r'comparisons-korea', ComparisonsKoreaViewSet, basename='korea-comparisons')


urlpatterns = [
    path('', include(router.urls)),
]
