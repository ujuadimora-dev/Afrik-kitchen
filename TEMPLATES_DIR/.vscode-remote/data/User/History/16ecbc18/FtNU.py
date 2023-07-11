from django.urls import path
from . import views
from django.urls import path
from .views import CreateEventView
from django.urls import path
from event import views
from .views import CreateEventView


urlpatterns = [
    path('create_event/', views.create_event, name='create_event'),
    # other URL patterns
]



