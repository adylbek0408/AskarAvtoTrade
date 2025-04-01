from django.contrib import admin
from .models import Korea, ComparisonsKorea
from apps.common.admin import BaseCarAdmin


@admin.register(Korea)
class KoreaAdmin(BaseCarAdmin):
    pass


@admin.register(ComparisonsKorea)
class ComparisonsKoreaAdmin(admin.ModelAdmin):
    list_display = ['id', 'korea_car', 'comparisons']
    list_filter = ['comparisons']
    search_fields = ['korea_car__brand__name', 'korea_car__model__name']
