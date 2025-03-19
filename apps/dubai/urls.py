from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DubaiViewSet, ComparisonsDubaiViewSet

app_name = 'dubai'

router = DefaultRouter()
router.register(r'cars', DubaiViewSet, basename='dubai-cars')
router.register(r'comparisons-dubai', ComparisonsDubaiViewSet, basename='dubai-comparisons')


urlpatterns = [
    path('', include(router.urls)),
]
