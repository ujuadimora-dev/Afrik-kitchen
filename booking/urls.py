from django.urls import path
from .views import create_booking

urlpatterns = [
    path('create_booking/', views.create_booking, name='create_booking'),
    
]

