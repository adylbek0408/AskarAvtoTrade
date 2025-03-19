from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Dubai, ComparisonsDubai
from apps.common.models import Interior, CarHistory, CarPhoto


@admin.register(ComparisonsDubai)
class ComparisonsDubaiAdmin(admin.ModelAdmin):
    list_display = ['id', 'dubai_car', 'comparisons']
    list_filter = ['comparisons']
    search_fields = ['america_car__brand__name', 'america_car__model__name']


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


@admin.register(Dubai)
class DubaiAdmin(admin.ModelAdmin):
    @admin.display(description='До начала аукциона')
    def time_until_auction(self, obj):
        return obj.time_until_auction()

    list_display = ('__str__', 'year', 'mileage', 'start_price', 'auction_start_time', 'time_until_auction')
    list_filter = ('brand', 'model', 'year', 'body_type', 'fuel_type', 'transmission_type')
    search_fields = ('brand__name', 'model__name', 'configuration', 'car_history__vin_code')
    readonly_fields = ('time_until_auction',)

    fieldsets = (
        ('Основная информация', {
            'fields': (
                ('brand', 'model'),
                'year',
                'mileage',
                'configuration',
                ('engine_volume', 'power'),
                ('color', 'body_type'),
                ('fuel_type', 'transmission_type'),
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
        super().save_model(request, obj, form, change)
        obj.save()

        if not Interior.objects.filter(content_type=ContentType.objects.get_for_model(obj), object_id=obj.id).exists():
            Interior.objects.create(
                content_object=obj,
                interior_color=obj.color,
                steering_wheel='regular',
                seat_material='leather'
            )

        if not CarHistory.objects.filter(content_type=ContentType.objects.get_for_model(obj),
                                         object_id=obj.id).exists():
            CarHistory.objects.create(
                content_object=obj,
                vin_code="Не указан",
                carfax_status="clean"
            )
