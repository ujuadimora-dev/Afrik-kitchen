from django.urls import path
from home.views import EventViewView

urlpatterns = [
    path('event/', EventView.as_view(), name='event')
    ]




