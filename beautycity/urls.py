from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('service/', views.make_order, name='make_order'),
    path('service_finally/', views.confirm_order, name='confirm_order'),
    path('get_free_time/', views.get_free_time, name='get_free_time'),
    path('reviews/', views.get_review, name='reviews'),
    path('get_masters/', views.get_masters, name='get_masters'),

    path('api/application/', views.get_application),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
