
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import EventForm

class CreateEventView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'event/create_event.html'
    success_url = '/event/success'  # Replace with your actual success UR

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            # Save the event to the database
            event = form.save()
            # Redirect to a success page or do further processing
            return redirect('event:success')
    else:
        form = EventForm()
    
    context = {'form': form}

