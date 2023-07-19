# from django.urls import path
# from event.views import EventView



# app_name = 'event'

# urlpatterns = [
#     path('event/', EventView.as_view(), name='event'


from django.urls import path

from . import views

app_name = 'event'

urlpatterns = [
    path('create/', views.create_event, name='create_event'),
    # other URL patterns for the 'event' namespace
]
