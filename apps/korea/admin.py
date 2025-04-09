from django.contrib import admin
from .models import Korea
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
