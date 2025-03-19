from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AmericaViewSet, ComparisonsAmericaViewSet

app_name = 'america'

router = DefaultRouter()
router.register(r'cars', AmericaViewSet, basename='america-cars')
router.register(r'comparisons-america', ComparisonsAmericaViewSet, basename='america-comparisons')


urlpatterns = [
    path('', include(router.urls)),
]
