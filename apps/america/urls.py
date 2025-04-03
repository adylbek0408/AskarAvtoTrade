from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AmericaViewSet, ComparisonsAmericaViewSet
from apps.common.views import CarBrandViewSet, CarModelViewSet, ManagerViewSet


app_name = 'america'

router = DefaultRouter()
router.register(r'cars', AmericaViewSet, basename='america-cars')
router.register(r'cars-brands', CarBrandViewSet, basename='brands-cars')
router.register(r'cars-model', CarModelViewSet, basename='model-cars')
router.register(r'managers', ManagerViewSet, basename='manager')
router.register(r'comparisons-america', ComparisonsAmericaViewSet, basename='america-comparisons')


urlpatterns = [
    path('', include(router.urls)),
]
