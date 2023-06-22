from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Booking
from booking.forms import BookingForm

class CreateBookingView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/booking.html'
    #success_url = '/booking/success.html/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SuccessView:
    def get_success(self):
        return redirect('/booking/success.html/')
    



        



