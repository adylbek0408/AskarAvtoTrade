from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
   openapi.Info(
      title="Car Parser API",
      default_version='v1',
      description="API для парсинга автомобилей с аукционов",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('administration-jylas-trade/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/america/', include('apps.america.urls')),
    path('api/korea/', include('apps.korea.urls')),
    path('api/dubai/', include('apps.dubai.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
