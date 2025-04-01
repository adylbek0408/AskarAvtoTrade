from django.contrib import admin
from .models import America, ComparisonsAmerica
from apps.common.admin import BaseCarAdmin


@admin.register(America)
class AmericaAdmin(BaseCarAdmin):
    pass


@admin.register(ComparisonsAmerica)
class ComparisonsAmericaAdmin(admin.ModelAdmin):
    list_display = ['id', 'america_car', 'comparisons']
    list_filter = ['comparisons']
    search_fields = ['america_car__brand__name', 'america_car__model__name']
