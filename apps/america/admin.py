from django.contrib import admin
from .models import America, ComparisonsAmerica
from apps.common.admin import BaseCarAdmin
from django import forms


class AmericaForm(forms.ModelForm):
    class Meta:
        model = America
        fields = '__all__'
        widgets = {
            'url': forms.URLInput(attrs={'required': False}),
        }


@admin.register(America)
class AmericaAdmin(BaseCarAdmin):
    form = AmericaForm



@admin.register(ComparisonsAmerica)
class ComparisonsAmericaAdmin(admin.ModelAdmin):
    list_display = ['id', 'america_car', 'comparisons']
    list_filter = ['comparisons']
    search_fields = ['america_car__brand__name', 'america_car__model__name']
