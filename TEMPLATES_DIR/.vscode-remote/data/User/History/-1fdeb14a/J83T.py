from django.urls import path
from .import views

app_name = 'view_menu'

urlpatterns = [
    path('menu', views.menu, name="menu"), # menu here is the url for the view_menu
  path('breakfast', views.menu, name="breakfast"),
]