from .models import CarBrand, CarModel, Color, Manager
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.contenttypes.models import ContentType
from .models import Interior, CarHistory, CarPhoto


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
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone_number']
    search_fields = ['full_name', 'phone_number']


class InteriorInline(GenericTabularInline):
    model = Interior
    ct_field = 'content_type'
    ct_fk_field = 'object_id'
    extra = 1
    max_num = 1


class CarHistoryInline(GenericTabularInline):
    model = CarHistory
    ct_field = 'content_type'
    ct_fk_field = 'object_id'
    extra = 1
    max_num = 1


class CarPhotoInline(GenericTabularInline):
    model = CarPhoto
    ct_field = 'content_type'
    ct_fk_field = 'object_id'
    extra = 3
    verbose_name = "Фотография"
    verbose_name_plural = "Фотографии"
    fields = ('image', 'is_main')  # Explicitly specify which fields to show

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        if obj:
            formset.form.initial = {
                'content_type': ContentType.objects.get_for_model(obj).pk,
                'object_id': obj.id
            }
        return formset


class BaseCarAdmin(admin.ModelAdmin):
    @admin.display(description='До начала аукциона')
    def time_until_auction(self, obj):
        return obj.time_until_auction()
    list_display = ('__str__', 'year', 'mileage', 'start_price', 'auction_start_time', 'time_until_auction')
    list_filter = ('brand', 'model', 'year', 'fuel_type', 'transmission_type')
    search_fields = ('brand__name', 'model__name', 'configuration', 'car_history__vin_code')
    readonly_fields = ('time_until_auction',)

    fieldsets = (
    ('Основная информация', {
        'fields': (
            ('brand', 'model'),
            'year',
            'mileage',
            'configuration',
            'engine_volume',
            'power',
            'color',
            ('fuel_type', 'body_type_choices'),
            ('transmission_type', 'drive_type')
        )
    }),
    ('Цена и аукцион', {
        'fields': (
            ('start_price', 'end_price'),
            'manager',
            'auction_start_time',
            'time_until_auction',
        )
    }),
    ('Ссылки', {
        'fields': ('url',),
    }),
    )

    inlines = [InteriorInline, CarHistoryInline, CarPhotoInline]

    def save_model(self, request, obj, form, change):
        obj.url = obj.url or ''
        super().save_model(request, obj, form, change)

        content_type = ContentType.objects.get_for_model(obj)

