# Generated by Django 4.2.1 on 2023-05-24 10:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('master_firstname', models.CharField(max_length=50, verbose_name='имя мастера')),
                ('master_lastname', models.CharField(blank=True, db_index=True, max_length=50, verbose_name='фамилия мастера')),
            ],
        ),
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='адрес')),
                ('image', models.ImageField(upload_to='images/', verbose_name='фото салона')),
                ('contact_phone', models.CharField(blank=True, max_length=50, verbose_name='контактный телефон')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('description', models.TextField(blank=True, max_length=200, verbose_name='описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0), django.core.validators.DecimalValidator(8, 2)], verbose_name='цена')),
                ('time_in_minute', models.IntegerField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services', to='shop.servicecategory', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'сервис',
                'verbose_name_plural': 'сервисы',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Время создания')),
                ('client_firstname', models.CharField(db_index=True, max_length=50, verbose_name='Имя клиента')),
                ('client_lastname', models.CharField(blank=True, db_index=True, max_length=50, verbose_name='Фамилия клиента')),
                ('client_phonenumber', phonenumber_field.modelfields.PhoneNumberField(db_index=True, max_length=128, region=None, verbose_name='Номер владельца')),
                ('client_comment', models.TextField(blank=True, verbose_name='Комментарий')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0), django.core.validators.DecimalValidator(8, 2)], verbose_name='цена')),
                ('payment', models.BooleanField(default=False, verbose_name='Оплачен')),
                ('master', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='shop.master', verbose_name='Мастер, который выполняет заказ')),
                ('salon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='shop.salon', verbose_name='Салон, где выполняют заказ')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='shop.service', verbose_name='Сервис')),
            ],
        ),
        migrations.AddField(
            model_name='master',
            name='salon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='masters', to='shop.salon', verbose_name='салон, где работает мастер'),
        ),
        migrations.CreateModel(
            name='MasterServiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability', models.BooleanField(db_index=True, default=True, verbose_name='доступен у мастера')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_items', to='shop.master', verbose_name='мастер')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_items', to='shop.service', verbose_name='сервис')),
            ],
            options={
                'verbose_name': 'сервис доступный у мастера',
                'verbose_name_plural': 'сервисы доступные у мастера',
                'unique_together': {('master', 'service')},
            },
        ),
    ]
