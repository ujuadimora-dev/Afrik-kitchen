
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import EventForm

def create_event(request):
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
    return render(request, 'event/create_event.html', context)
