from django.urls import path
from . import views
from django.urls import path
from .views import CreateEventView
from django.urls import path
from event import views

urlpatterns = [
    path('create_event/', views.create_event, name='create_event'),
    # other URL patterns
]


# app_name = 'event'

# urlpatterns = [
#     path('create/', CreateEventView.as_view(), name='CreateEventView'),
#     # Other URL patterns for the 'event' namespace
# ]

