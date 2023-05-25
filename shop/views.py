from django.http import JsonResponse
from django.shortcuts import render

from .models import Salon, Service, Master


def index(request):
    salons = Salon.objects.all()
    services = Service.objects.all()
    masters = Master.objects.all()
    context = {
        'salons': salons,
        'services': services,
        'masters': masters,
    }
    return render(request, 'index.html', context)


def make_order(request):
    context = {}
    return render(request, 'service.html', context)


def confirm_order(request):
    context = {}
    return render(request, 'service_finally.html', context)


def get_free_time(request):
    # Получение выбранной даты из параметров запроса
    selected_date = request.GET.get('date')

    free_time = {
        'Утро': ['10:00', '10:30', '11:00', '11:30',],
        'День': ['12:00', '12:30', ],
        'Вечер': ['17:00', '18:00']
    }

    return JsonResponse(free_time)
