# Generated by Django 4.2.1 on 2023-05-24 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='master',
            options={'verbose_name': 'мастер', 'verbose_name_plural': 'мастера'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'заказ', 'verbose_name_plural': 'заказы'},
        ),
        migrations.AlterModelOptions(
            name='salon',
            options={'verbose_name': 'салон', 'verbose_name_plural': 'салоны'},
        ),
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='фото услуги'),
        ),
        migrations.AlterField(
            model_name='salon',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='фото салона'),
        ),
    ]