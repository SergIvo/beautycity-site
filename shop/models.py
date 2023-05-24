from django.db import models
from django.core.validators import MinValueValidator, DecimalValidator
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Salon(models.Model):
    name = models.CharField(
        'название',
        max_length=50
    )
    address = models.CharField(
        'адрес',
        max_length=100,
        blank=True,
    )
    image = models.ImageField(
        'фото салона',
        null=True,
        blank=True,
        upload_to='images/',
    )
    contact_phone = models.CharField(
        'контактный телефон',
        max_length=50,
        blank=True,
    )

    class Meta:
        verbose_name = 'салон'
        verbose_name_plural = 'салоны'

    def __str__(self):
        return self.name


class Master(models.Model):
    master_firstname = models.CharField(
        'имя мастера',
        max_length=50
    )
    master_lastname = models.CharField(
        'фамилия мастера',
        max_length=50,
        blank=True,
        db_index=True,
    )
    salon = models.ForeignKey(
        Salon,
        verbose_name='салон, где работает мастер',
        related_name='masters',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = 'мастер'
        verbose_name_plural = 'мастера'

    def __str__(self):
        return self.master_firstname


class ServiceCategory(models.Model):
    name = models.CharField(
        'название',
        max_length=50
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class ServiceQuerySet(models.QuerySet):
    def available(self):
        services = (
            MasterServiceItem.objects
            .filter(availability=True)
            .values_list('services')
        )
        return self.filter(pk__in=services)


class Service(models.Model):
    name = models.CharField(
        'название',
        max_length=50
    )
    category = models.ForeignKey(
        ServiceCategory,
        verbose_name='категория',
        related_name='services',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    description = models.TextField(
        'описание',
        max_length=200,
        blank=True,
    )
    price = models.DecimalField(
        'цена',
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0), DecimalValidator(8, 2)]
    )
    image = models.ImageField(
        'фото услуги',
        null=True,
        blank=True,
        upload_to='images/',
    )
    time_in_minute = models.IntegerField()

    objects = ServiceQuerySet.as_manager()

    class Meta:
        verbose_name = 'сервис'
        verbose_name_plural = 'сервисы'

    def __str__(self):
        return self.name


class MasterServiceItem(models.Model):
    master = models.ForeignKey(
        Master,
        related_name='service_items',
        verbose_name="мастер",
        on_delete=models.CASCADE,
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='service_items',
        verbose_name='сервис',
    )
    availability = models.BooleanField(
        'доступен у мастера',
        default=True,
        db_index=True
    )

    class Meta:
        verbose_name = 'сервис доступный у мастера'
        verbose_name_plural = 'сервисы доступные у мастера'
        unique_together = [
            ['master', 'service']
        ]

    def __str__(self):
        return f"{self.master.master_firstname} - {self.service.name}"


class Order(models.Model):
    salon = models.ForeignKey(
        Salon,
        verbose_name='Салон, где выполняют заказ',
        related_name='orders',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    master = models.ForeignKey(
        Master,
        verbose_name='Мастер, который выполняет заказ',
        related_name='orders',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    service = models.ForeignKey(
        Service,
        verbose_name='Сервис',
        related_name='orders',
        on_delete=models.PROTECT,
    )
    registered_at = models.DateTimeField(
        'Время создания',
        db_index=True,
        default=timezone.now,
    )
    client_firstname = models.CharField(
        'Имя клиента',
        max_length=50,
        db_index=True,
    )
    client_lastname = models.CharField(
        'Фамилия клиента',
        max_length=50,
        blank=True,
        db_index=True,
    )
    client_phonenumber = PhoneNumberField(
        'Номер владельца',
        db_index=True,
    )
    client_comment = models.TextField(
        'Комментарий',
        blank=True,
    )
    price = models.DecimalField(
        'цена',
        max_digits=8,
        decimal_places=2,
        blank=True,
        validators=[MinValueValidator(0), DecimalValidator(8, 2)],
    )
    payment = models.BooleanField('Оплачен', default=False)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return self.client_firstname
