from django.urls import path
from . import views

app_name = 'partners'

urlpatterns = [
    path('new/', views.create_partner, name='new_partner'),
    path('', views.partners, name='partners'),
    path('info/<int:pk>/', views.info_partner, name='info_partner'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('edit/<int:pk>/', views.edit, name='edit_partner')
]