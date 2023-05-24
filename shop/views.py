from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'index.html', context)


def make_order(request):
    context = {}
    return render(request, 'service.html', context)


def confirm_order(request):
    context = {}
    return render(request, 'service_finally.html', context)
