from django.shortcuts import render

from datetime import timedelta, date
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView, CreateView, UpdateView, ListView
from django.contrib import messages
from .models import Booking, Table
from .forms import BookingForm


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking, Customer, Table
from .forms import BookingForm

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer_name = Customer.objects.get(pk=request.POST['customer'])
            booking.save()
            messages.success(request, 'Booking created successfully.')
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'booking/create_booking.html', {'form': form})

def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer_name = Customer.objects.get(pk=request.POST['customer'])
            booking.save()
            messages.success(request, 'Booking updated successfully.')
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking/edit_booking.html', {'form': form, 'booking': booking})

def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking canceled successfully.')
        return redirect('booking_list')
    return render(request, 'booking/cancel_booking.html', {'booking': booking})

def rebook_booking(request, booking_id):
    old_booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            new_booking = form.save(commit=False)
            new_booking.customer_name = old_booking.customer_name
            new_booking.save()
            old_booking.delete()
            messages.success(request, 'Booking rebooked successfully.')
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'booking/rebook_booking.html', {'form': form, 'old_booking': old_booking})

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking/booking_list.html', {'bookings': bookings})
