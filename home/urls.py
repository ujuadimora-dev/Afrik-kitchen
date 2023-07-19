from django.urls import path
from home.views import HomeView
from afrik_kitchen.views import contact, success

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', contact, name='contact'),
    path('contact_success/{name}/', success, name='contact_success')

    ]


