from django.db import models


class Salon(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Master(models.Model):
    name = models.CharField(max_length=200)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    SERVICE_CATEGORIES = (
        ('Мастер маникюра', 'Мастер маникюра'),
        ('Парикмахер', 'Парикмахер'),
        ('Визажист', 'Визажист'),
        ('Стилист', 'Стилист'),
    )
    service_category = models.CharField(max_length=200, choices=SERVICE_CATEGORIES)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=200)
    SERVICE_TYPE = (
        ('Парикмахерские услуги', 'Парикмахерские услуги'),
        ('Ногтевой сервис', 'Ногтевой сервис'),
        ('Макияж', 'Макияж'),
    )
    service_type = models.CharField(max_length=200, choices=SERVICE_TYPE)
    masters = models.ManyToManyField(Master)
    price = models.IntegerField()
    time_in_minute = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField()
    client_name = models.CharField(max_length=200)
    client_phone = models.CharField(max_length=200)
    client_comment = models.CharField(max_length=200)
    payment = models.BooleanField(default=False)

    def __str__(self):
        return self.client_name
