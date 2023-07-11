from django.urls import path
from . import views



app_name = 'event'

urlpatterns = [
    path('create/', views.create_event, name='create_event'),
    
]

from django.urls import path
from . import CreateEventView

app_name = 'event'

urlpatterns = [
    path('create/', CreateEventView.as(), name='create_event'),
   
]

