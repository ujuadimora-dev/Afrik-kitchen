"""afrik_kitchen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from view_menu import views
from django.conf import settings
from django.conf.urls.static import static
#from booking.views import create_booking
#from booking import views
#from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



#from django.urls import path
#from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    #path('', include('view.urls')),
    path('view_menu', include('view_menu.urls', namespace='view_menu')),
    path('booking/create_booking/', create_booking, name='create_booking'),
    path('booking/', include('booking.urls', namespace='booking')),
]


#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 



#path('admin/', admin.site.urls),
    #path('', include('home.urls')),
    #path('booking/', include('booking.urls')),
    #path('menu/', include('menu.urls')),