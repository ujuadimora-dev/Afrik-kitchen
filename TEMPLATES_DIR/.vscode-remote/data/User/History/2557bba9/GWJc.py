from django.urls import path
from home.views import HomeView
from home.views import contact


app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', contact, name='contact'),
    ]


