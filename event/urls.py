from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'event'

urlpatterns = [
    path('', views.actual_events, name='main_page'),
    path('new_event/', views.create_event, name='new_event')
]