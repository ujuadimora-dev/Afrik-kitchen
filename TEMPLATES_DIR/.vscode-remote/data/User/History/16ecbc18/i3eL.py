from django.urls import path
from . import views
from django.urls import path
from .views import CreateEventView

app_name = 'event'

urlpatterns = [
    path('create/', CreateEventView.as_view(), name='CreateEventView'),
    # Other URL patterns for the 'event' namespace
]

