
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import EventForm

from django.views.generic import CreateView
from .models import Event
from .forms import EventForm

class CreateEventView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'event/create_event.html'
    success_url = '/event/success'  # Replace with your actual success URL

    def form_valid(self, form):
        # Save the event to the database
        event = form.save()
        # Redirect to a success page or do further processing
        return super().form_valid(form)
