from django.contrib import admin
from .models import Service, ServiceCategory
from .models import Salon
from .models import Master, MasterServiceItem
from .models import Order
from .models import Application


class MasterServiceItemInline(admin.TabularInline):
    model = MasterServiceItem
    extra = 0


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    search_fields = [
        'master_firstname',
        'master_lastname',
    ]
    list_display = [
        'master_firstname',
        'master_lastname',
    ]
    list_filter = [
        'salon',
    ]
    inlines = [
        MasterServiceItemInline
    ]


@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'address',
        'contact_phone',
    ]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'category',
        'price',
    ]
    list_display_links = [
        'name',
    ]
    list_filter = [
        'category',
    ]
    search_fields = [
        'name',
        'category__name',
    ]

    inlines = [
        MasterServiceItemInline
    ]


@admin.register(ServiceCategory)
class ServiceCategory(admin.ModelAdmin):
    list_display = [
        'name',
    ]


@admin.register(Order)
class Order(admin.ModelAdmin):
    search_fields = ('client_firstname', 'client_lastname', 'salon', 'master', 'client_phonenumber')
    list_display = ('client_firstname', 'client_lastname', 'payment', 'client_phonenumber')
    list_filter = ('client_phonenumber', 'payment')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
        'phonenumber',
    ]
    list_display = [
        'name',
        'phonenumber',
        'registered_at',
        'processed',
    ]
    list_filter = [
        'phonenumber',
        'registered_at',
        'processed',
    ]
