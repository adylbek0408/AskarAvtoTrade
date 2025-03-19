from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AmericaViewSet

app_name = 'america'

router = DefaultRouter()
router.register(r'cars', AmericaViewSet, basename='america-cars')

urlpatterns = [
    path('', include(router.urls)),
]
