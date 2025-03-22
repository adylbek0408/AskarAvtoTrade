from django.db import models
from django.utils import timezone
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class CarBrand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Марка")
    logo = models.ImageField(upload_to='brands/logos/', verbose_name="Логотип")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Марка автомобиля"
        verbose_name_plural = "Марки автомобилей"


class CarModel(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='models', verbose_name="Марка")
    name = models.CharField(max_length=100, verbose_name="Модель")

    def __str__(self):
        return f"{self.brand.name} {self.name}"

    class Meta:
        verbose_name = "Модель автомобиля"
        verbose_name_plural = "Модели автомобилей"


class Color(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название цвета")
    hex_code = models.CharField(max_length=7, verbose_name="Код цвета (HEX)", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"


class BodyType(models.Model):
    name = models.CharField(max_length=50, verbose_name="Тип кузова")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип кузова"
        verbose_name_plural = "Типы кузовов"


class Manager(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    whatsapp_url = models.URLField(verbose_name="Ссылка на WhatsApp")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Менеджер"
        verbose_name_plural = "Менеджеры"


class Interior(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    STEERING_WHEEL_CHOICES = [
        ('right', 'Правый'),
        ('left', 'Левый'),
    ]

    SEAT_MATERIAL_CHOICES = [
        ('leather', 'Кожаный'),
        ('velour', 'Велюр'),
        ('combined', 'Комбинированный'),
        ('cloth', 'Тряпичный'),
    ]

    steering_wheel = models.CharField(max_length=20, choices=STEERING_WHEEL_CHOICES, verbose_name="Руль")
    interior_color = models.ForeignKey(Color, on_delete=models.PROTECT, related_name='interiors',
                                       verbose_name="Цвет салона")
    seat_material = models.CharField(max_length=20, choices=SEAT_MATERIAL_CHOICES, verbose_name="Материал сидений")

    class Meta:
        verbose_name = "Интерьер"
        verbose_name_plural = "Интерьеры"


class CarHistory(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    CARFAX_CHOICES = [
        ('clean', 'Чистый'),
        ('dirty', 'Не чистый'),
    ]

    carfax_status = models.CharField(max_length=10, choices=CARFAX_CHOICES, verbose_name="Статус Carfax")
    vin_code = models.CharField(max_length=17, verbose_name="VIN код")

    class Meta:
        verbose_name = "История автомобиля"
        verbose_name_plural = "Истории автомобилей"


class CarPhoto(models.Model):
    image = models.ImageField(upload_to='cars/photos/', verbose_name="Фото")
    is_main = models.BooleanField(default=False, verbose_name="Основное фото")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"Фото {self.id}"

    class Meta:
        verbose_name = "Фото автомобиля"
        verbose_name_plural = "Фото автомобилей"


class Car(models.Model):
    FUEL_TYPE_CHOICES = [
        ('petrol', 'Бензин'),
        ('diesel', 'Дизель'),
        ('hybrid', 'Гибрид'),
        ('electric', 'Электрический'),
        ('hydrogen', 'Водород'),
    ]

    TRANSMISSION_TYPE_CHOICES = [
        ('manual', 'Механическая'),
        ('automatic', 'Автоматическая'),
        ('robot', 'Роботизированная'),
        ('variator', 'Вариатор'),
        ('dsg', 'DSG (Робот с двойным сцеплением)'),
    ]

    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, verbose_name="Марка")
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name="Модель")
    year = models.PositiveIntegerField(verbose_name="Год выпуска", db_index=True)
    mileage = models.PositiveIntegerField(verbose_name="Пробег (км)", db_index=True)
    engine_volume = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Объем двигателя (л)")
    power = models.PositiveIntegerField(verbose_name="Мощность (л.с.)")
    configuration = models.CharField(max_length=255, verbose_name="Комплектация")
    color = models.ForeignKey(Color, on_delete=models.PROTECT, verbose_name="Цвет")
    body_type = models.ForeignKey(BodyType, on_delete=models.PROTECT, verbose_name="Тип кузова")
    fuel_type = models.CharField(max_length=20, choices=FUEL_TYPE_CHOICES, verbose_name="Тип топлива")
    transmission_type = models.CharField(max_length=20, choices=TRANSMISSION_TYPE_CHOICES, verbose_name="Тип КПП")
    start_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Начальная цена", db_index=True)
    end_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Конечная цена", blank=True,
                                    null=True)
    manager = models.ForeignKey(Manager, on_delete=models.PROTECT, verbose_name="Менеджер")
    auction_start_time = models.DateTimeField(
        verbose_name="Время начала аукциона",
        default=timezone.now
    )

    def time_until_auction(self):
        if not self.auction_start_time:  # Handle None case
            return "Время аукциона не установлено"

        now = timezone.now()
        if now > self.auction_start_time:
            return "Аукцион уже начался"

    @property
    def interior(self):
        return Interior.objects.filter(
            content_type=ContentType.objects.get_for_model(self),
            object_id=self.id
        ).first()

    @property
    def car_history(self):
        return CarHistory.objects.filter(
            content_type=ContentType.objects.get_for_model(self),
            object_id=self.id
        ).first()

    @property
    def photos(self):
        return CarPhoto.objects.filter(
            content_type=ContentType.objects.get_for_model(self.__class__),
            object_id=self.id
        )

    def __str__(self):
        return f"{self.brand.name} {self.model.name} ({self.year})"

    def time_until_auction(self):
        now = timezone.now()
        if now > self.auction_start_time:
            return "Аукцион уже начался"

        time_delta = self.auction_start_time - now
        days = time_delta.days
        hours, remainder = divmod(time_delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        return f"{days} дней, {hours} часов, {minutes} минут, {seconds} секунд"

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"
        abstract = True
