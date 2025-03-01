from django.urls import path
from . import views

app_name = 'feedback'

urlpatterns = [
    path('feedback/', views.feedback, name='feedback'),
    path('feedback_info/', views.feedback_info, name='feedback_info')
]