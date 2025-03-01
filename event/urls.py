from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'event'

urlpatterns = [
    path('', views.actual_events, name='main_page'),
    path('new_event/', views.create_event, name='new_event'),
    path('cart_add/<int:pk>/', views.add_event, name='add_event'),
    path('user_cart/', views.my_user_event, name='user_event'),
    path('admin_cart/', views.my_admin_event, name='admin_event'),
    path('info_event/<int:pk>/', views.info_event, name='info_event'),
]