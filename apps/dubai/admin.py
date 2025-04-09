from django.contrib import admin
from .models import Dubai, ComparisonsDubai
from apps.common.admin import BaseCarAdmin
from django import forms


class DubaiForm(forms.ModelForm):
    class Meta:
        model = Dubai
        fields = '__all__'
        widgets = {
            'url': forms.URLInput(attrs={'required': False}),
        }


@admin.register(Dubai)
class DubaiAdmin(BaseCarAdmin):
    form = DubaiForm


@admin.register(ComparisonsDubai)
class ComparisonsDubaiAdmin(admin.ModelAdmin):
    list_display = ['id', 'dubai_car', 'comparisons']
    list_filter = ['comparisons']
    search_fields = ['dubai_car__brand__name', 'dubai_car__model__name']
