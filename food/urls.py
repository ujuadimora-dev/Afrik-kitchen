from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path('', views.food, name='food'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    # path('menu_list/', views.food, name='menu_list'),

    path('add/', views.create_menuitem, name='create_menuitem'),
    path('delete/<int:pk>/', views.delete_menuitem, name='delete_menuitem'),
    path('update/<int:pk>/', views.update_menuitem, name='update_menuitem'),
    path('manage_menu/', views.manage_menu, name='manage_menu'),
]

