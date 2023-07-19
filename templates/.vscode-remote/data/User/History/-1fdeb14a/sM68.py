from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



app_name = 'view_menu'

urlpatterns = [
    path('menu/', views.menu, name="menu"),   # menu here is the url for the view_menu
    path('breakfast/', views.breakfast, name="breakfast"),
    path('lunch/', views.lunch, name="lunch"),
]

# Add the following line at the end of the file
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
