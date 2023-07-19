from django.urls import path
from event.views import EventView

urlpatterns = [
    path('event/', EventView.as_view(), name='event')
    ]




