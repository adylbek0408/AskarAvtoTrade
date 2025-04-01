from django.contrib import admin
from .models import Korea, ComparisonsKorea
from apps.common.admin import BaseCarAdmin
from django import forms


class KoreaForm(forms.ModelForm):
    class Meta:
        model = Korea
        fields = '__all__'
        widgets = {
            'url': forms.URLInput(attrs={'required': False}),
        }


@admin.register(Korea)
class KoreaAdmin(BaseCarAdmin):
    form = KoreaForm


@admin.register(ComparisonsKorea)
class ComparisonsKoreaAdmin(admin.ModelAdmin):
    list_display = ['id', 'korea_car', 'comparisons']
    list_filter = ['comparisons']
    search_fields = ['korea_car__brand__name', 'korea_car__model__name']
