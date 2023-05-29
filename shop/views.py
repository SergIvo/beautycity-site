from datetime import datetime, timedelta

from django.db.models import Q, Sum
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from rest_framework.decorators import api_view
from .serializers import ApplicationSerializer, ReviewSerializer

from .models import Salon, Service, Master, Order, ServiceCategory, Review

from django.contrib.auth.decorators import user_passes_test


@api_view(['POST', 'GET'])
def index(request):
    salons = Salon.objects.all()
    services = Service.objects.all()
    masters = Master.objects.all()
    reviews = Review.objects.all()
    context = {
        'salons': salons,
        'services': services,
        'masters': masters,
        'reviews': reviews,
        'user_authorised': request.user.is_authenticated,
    }
    if request.method == 'POST':
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return render(request, 'success_application.html')
        else:
            context['serializer'] = serializer
            return render(request, 'index.html', context)

    return render(request, 'index.html', context)


@api_view(['POST', 'GET'])
def get_review(request):
    context = {}
    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return render(request, 'success_review.html')
        else:
            return render(request, 'reviews.html', context)
    return render(request, 'reviews.html', context)


def is_manager(user):
    return user.is_staff


@user_passes_test(is_manager, login_url='index')
def view_admin(request):
    total_payment_orders = Order.objects.filter(payment=True).count()
    total_orders = Order.objects.count()
    costs = Order.objects.filter(payment=True).aggregate(totals=Sum('price')).get('totals')
    context = {
        'user_authorised': request.user.is_authenticated,
        'total_payment_orders': total_payment_orders,
        'total_orders': total_orders,
        'costs': costs,
    }
    return render(request, 'admin.html', context)


def get_confidential(request):
    context = {}
    return render(request, 'confidential.html', context)


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
    datetime_str = f"{year}-{month}-{day} {time}"
    datetime_order = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")

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
        'salon_id': salon_id,
        'service_id': service_id,
        'master_id': master_id,
        'datetime_order': datetime_str,
    }

    return render(request, 'service_finally.html', context)


def order(request):
    print(request.POST.dict())
    master_id = request.POST.get('master_id')
    service_id = request.POST.get('service_id')
    salon_id = request.POST.get('salon_id')
    service=Service.objects.get(id=service_id)
    time = datetime.strptime(request.POST.get('datetime_order'), "%Y-%m-%d %H:%M")
    
    new_order = Order(
        salon=Salon.objects.get(id=salon_id),
        master=Master.objects.get(id=master_id),
        service=service,
        registered_at=time,
        client_firstname=request.POST.get('fname'),
        client_phonenumber=request.POST.get('tel'),
        client_comment=request.POST.get('contactsTextarea'),
        price=service.price
    )
    new_order.save()
    context = {
        'order': new_order,
        'time': time.strftime('%H:%M'),
        'year': time.year,
        'month': time.month,
        'day': time.day
    }
    
    return render(request, 'order_finally.html', context)


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
