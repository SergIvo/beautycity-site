from django.shortcuts import render
from .models import Salon, Service


def index(request):
    salons = Salon.objects.all()
    services = Service.objects.all()
    context = {
        'salons': salons,
        'services': services
    }
    return render(request, 'index.html', context)


def make_order(request):
    context = {}
    return render(request, 'service.html', context)


def confirm_order(request):
    context = {}
    return render(request, 'service_finally.html', context)
