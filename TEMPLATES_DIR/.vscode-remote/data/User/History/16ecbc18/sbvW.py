from django.urls import path
from home.views import EventView

urlpatterns = [
    path('event/', EventView.as_view(), name='event')
    ]




