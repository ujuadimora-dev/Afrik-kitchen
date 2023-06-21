from django.shortcuts import render
from datetime import timedelta, date
from  django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView
from .models import Booking, CreateTable
from .forms import BookingForm
# Create your views here.

""" This is the view for user creating  booking """
def create_booking(LoginRequiredMixin, CreateView):
    if request.method == 'POST':
        form = BookingForm(reqest.POST)
        if form.is_vakid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking/success.html')
        else:
            form = BookingForm()
        
        context = {'form': form}
        return render(request, 'booking/booking.html', context)


