from django.urls import path
from event.views import EventView
from .views import event

app_name = 'event'

urlpatterns = [
    path('event/', EventView.as_view(), name='event')
]




