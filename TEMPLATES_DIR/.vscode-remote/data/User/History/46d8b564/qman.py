
from django.shortcuts import render
from django.views.generic import TemplateView

class EventView(TemplateView):
    template_name = 'event/event.html'

