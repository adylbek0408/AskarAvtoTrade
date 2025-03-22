from django.contrib import admin
from .models import CarBrand, CarModel, Color, BodyType, Manager


@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'name']
    search_fields = ['brand__name', 'name']
    list_filter = ['brand']


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'hex_code']
    search_fields = ['name']


@admin.register(BodyType)
class BodyTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone_number']
    search_fields = ['full_name', 'phone_number']
