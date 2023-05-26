from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('service/', views.make_order, name='make_order'),
    path('get_free_time/', views.get_free_time, name='get_free_time'),
    path('pre_order/', views.pre_order, name='pre_order'),
    path('order/', views.order, name='order'),
    path('reviews/', views.get_review, name='reviews'),
    path('get_masters/', views.get_masters, name='get_masters'),
    path('manager/admin/', views.view_admin, name="admin"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
