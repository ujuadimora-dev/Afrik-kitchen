from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from .models import Booking, CreateTable, ManageBooking
from booking.forms import BookingForm


class CreateTableList(ListView):
    """ This is to book table for reservation"""
    model = CreateTable


class BookingList(ListView):
    """ This is show the booked Table"""
    model = Booking


class ManageBookingList(ListView):
    """ To manage the book table( delet, conceal, rebook)"""
    model = ManageBooking




    

        



