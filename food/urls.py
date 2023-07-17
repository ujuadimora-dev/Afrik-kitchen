from django.urls import path
from . import views




app_name = 'food'

urlpatterns = [
    path('', views.food, name='food'),

    path('detail/<int:pk>/', views.detail, name='detail'),
    path("add/", views.create_menuitem, name=create_menuitem)
  
]
