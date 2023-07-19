from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import create_menu
from view_menu import views






app_name = 'view_menu'

urlpatterns = [
    path('menu/', views.menu, name="menu"),   # menu here is the url for the view_menu
    path('breakfast/', views.breakfast, name="breakfast"),
    path('lunch/', views.lunch, name="lunch"),
    path('dinner/', views.dinner, name="dinner"),
    path('side/', views.side, name="side"),
    #path('create-menu/', views.create_menu, name='create_menu'),
    path('create-menu/', create_menu, name='create_menu')
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

