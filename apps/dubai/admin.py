from django.contrib import admin
from .models import Dubai, ComparisonsDubai
from apps.common.admin import BaseCarAdmin


@admin.register(Dubai)
class DubaiAdmin(BaseCarAdmin):
    pass


@admin.register(ComparisonsDubai)
class ComparisonsDubaiAdmin(admin.ModelAdmin):
    list_display = ['id', 'dubai_car', 'comparisons']
    list_filter = ['comparisons']
    search_fields = ['dubai_car__brand__name', 'dubai_car__model__name']
