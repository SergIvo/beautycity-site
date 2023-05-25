from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from .models import Salon, Service, Master

from rest_framework.decorators import api_view
from rest_framework.response import Response


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


def get_review(request):
    context = {}
    return render(request, 'reviews.html', context)


@api_view(['POST'])
def get_application(request):
    print(request.data)
    return Response(request.data)


def make_order(request):
    context = {}
    return render(request, 'service.html', context)


def confirm_order(request):
    context = {}
    return render(request, 'service_finally.html', context)


def get_free_time(request):
    # Получение выбранной даты из параметров запроса
    selected_day = request.GET.get('day')
    selected_month = request.GET.get('month')
    selected_year = request.GET.get('year')
    selected_master_id = request.GET.get('master')
    if selected_day == '1':
        free_time = {
            'Утро': ['10:00', ],
            'День': ['12:00', ],
            'Вечер': ['17:00',]
        }
    else:
        free_time = {
            'Утро': ['10:00', '10:30', '11:00', '11:30',],
            'День': ['12:00', '12:30', ],
            'Вечер': ['17:00', '18:00']
        }

    return JsonResponse(free_time)


def get_masters(request):
    address = request.GET.get('address')
    if address:
        salon = Salon.objects.get(address=address)
        masters = list(salon.masters.all())
        rendered = render_to_string('masters_list.html', {'masters': masters})
        html_response = HttpResponse(rendered)
    else:
        html_response = HttpResponse()
    return html_response
