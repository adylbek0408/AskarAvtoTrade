from django.contrib import admin
from .models import Dubai
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
