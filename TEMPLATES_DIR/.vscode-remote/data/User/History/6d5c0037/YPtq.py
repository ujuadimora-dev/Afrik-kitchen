from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import create_menu
from django.views import defaults as default_views
#from django.urls import handler404
from view_menu.views import page_not_found




app_name = 'view_menu'

urlpatterns = [
    path('menu/', views.menu, name="menu"),   
    path('breakfast/', views.breakfast, name="breakfast"),
    path('lunch/', views.lunch, name="lunch"),
    path('dinner/', views.dinner, name="dinner"),
    path('side/', views.side, name="side"),
    path('create-menu/', views.create_menu, name='create_menu')
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


