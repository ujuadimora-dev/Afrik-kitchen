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
# # from django.contrib import admin
# from django.urls import path, include
# from view_menu import views
# from django.conf import settings
# from django.conf.urls.static import static
# #from booking.views import create_booking
# #from booking.views import CreateBookingView
# #from booking import views
# #from . import views
# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from django.urls import path, include
# from django.contrib import admin
# #from view_menu import views
# #from booking import views
# from booking import views



# #from django.urls import path
# #from . import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='index'),
#     #path('', include('view.urls')),
#     path('view_menu/', include('view_menu.urls', namespace='view_menu')),
#     #path('booking/', include(('booking.urls', 'booking'), namespace='booking')),
#     #path('booking/', include('booking.urls', namespace='booking')),
#     path('booking/', include(('booking.urls', 'booking'), namespace='booking')),


#    #path('booking/', include('booking.urls', namespace='booking')),
#     #path('booking/', include('booking.urls', namespace='booking')),
    
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 




from django.contrib import admin
from django.urls import path, include
from view_menu import views
from django.conf import settings
from django.conf.urls.static import static
from view_menu import views as view_menu_views
from booking import views as booking_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('view_menu/', include('view_menu.urls', namespace='view_menu')),
    path('', booking.index, name='index'),
    path('booking/', include(('booking.urls', 'booking'), namespace='booking')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



  
rom django.contrib import admin
from django.urls import path, include
from view_menu import views as view_menu_views
from booking import views as booking_views
from django.conf import settings
from django.conf.urls.static import static
