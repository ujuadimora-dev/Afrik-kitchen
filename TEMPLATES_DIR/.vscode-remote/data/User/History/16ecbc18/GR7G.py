from django.urls import path
from . import views



app_name = 'event'

urlpatterns = [
    path('create/', views.create_event, name='create_event'),
    
]

from django.urls import path
from . import views

app_name = 'event'

urlpatterns = [
    path('create/', views.create_event, name='create_event'),
    # Other URL patterns for the 'event' namespace
]

