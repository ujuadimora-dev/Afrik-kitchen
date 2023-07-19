from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import create_menu,  page_not_found, permission_denied



app_name = 'view_menu'

urlpatterns = [
    path('menu/', views.menu, name="menu"),   
    path('breakfast/', views.breakfast, name="breakfast"),
    path('lunch/', views.lunch, name="lunch"),
    path('dinner/', views.dinner, name="dinner"),
    path('side/', views.side, name="side"),
    path('create-menu/', views.create_menu, name='create_menu'),
    path('view_menu/create-menu/includes/403.html', permission_denied, name='403'),
    path('page_not_found/', page_not_found, name='page_not_found')
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.urls import path
from .views import permission_denied

urlpatterns = [
    # Other URL patterns
    path('view_menu/create-menu/includes/403.html', permission_denied, name='403'),
]
