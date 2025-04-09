from django.contrib import admin
from .models import America
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
