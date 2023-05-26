from datetime import datetime, timedelta

from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ApplicationSerializer

from .models import Salon, Service, Master, Order, ServiceCategory

from django.contrib.auth.decorators import user_passes_test


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
    serializer = ApplicationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    serializer.save()

    return render(request, 'success_application.html')


def is_manager(user):
    return user.is_staff


@user_passes_test(is_manager, login_url='shop:index')
def view_admin(request):
    context = {}
    return render(request, 'admin.html', context)


def make_order(request):
    salons = Salon.objects.all()
    categories = ServiceCategory.objects.all()
    for category in categories:
        category.service_list = category.services.all()
    context = {
        'salons': salons,
        'categories': categories
    }
    return render(request, 'service.html', context)


def confirm_order(request):
    context = {}
    return render(request, 'service_finally.html', context)


def get_free_time(request):
    selected_day = int(request.GET.get('day'))
    selected_month = int(request.GET.get('month'))
    selected_year = int(request.GET.get('year'))
    selected_master_id = request.GET.get('master_id')
    selected_date = datetime(selected_year, selected_month, selected_day)

    # список всех возможных временных слотов
    time_slots = [
        (datetime.combine(selected_date, datetime.min.time()) + timedelta(hours=10, minutes=30 * i)).time()
        for i in range(20)  # 20 полу-часовых слотов с 10:00 до 20:00
    ]
    # если выбран мастер
    if selected_master_id != 'null':
        # получаем заказы мастера на эту дату
        orders = Order.objects.filter(
            Q(master__id=selected_master_id),
            Q(registered_at__year=selected_year),
            Q(registered_at__month=selected_month),
            Q(registered_at__day=selected_day),
        )

        # удаляем занятые временные слоты
        for order in orders:
            if order.registered_at.time() in time_slots:
                time_slots.remove(order.registered_at.time())

    free_time = {
        'Утро': [ts.strftime('%H:%M') for ts in time_slots if 10 <= ts.hour < 12],
        'День': [ts.strftime('%H:%M') for ts in time_slots if 12 <= ts.hour < 17],
        'Вечер': [ts.strftime('%H:%M') for ts in time_slots if 17 <= ts.hour < 20],
    }

    return JsonResponse(free_time)


def pre_order(request):
    day = request.GET.get('day')
    month = request.GET.get('month')
    year = request.GET.get('year')
    time = request.GET.get('time')
    master_id = request.GET.get('master_id')
    service_id = request.GET.get('service_id')
    salon_id = request.GET.get('salon_id')

    master = Master.objects.get(id=master_id)
    service = Service.objects.get(id=service_id)
    salon = Salon.objects.get(id=salon_id)

    order_number = Order.objects.all().order_by('-id').first()

    if order_number is not None:
        order_number = order_number.id + 1
    else:
        order_number = 1

    context = {
        'day': day,
        'month': month,
        'year': year,
        'time': time,
        'master': master,
        'service': service,
        'salon': salon,
        'order_number': order_number,
    }

    return render(request, 'service_finally.html', context)


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
