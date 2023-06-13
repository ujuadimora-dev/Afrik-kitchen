from django.urls import path
from .import views

app_name = 'view_menu'

urlpatterns =[
    path('menu', views.menu, name="menu"),
]