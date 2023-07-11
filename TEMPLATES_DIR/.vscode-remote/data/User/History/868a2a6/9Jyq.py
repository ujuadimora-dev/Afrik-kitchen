# from django.shortcuts import render

# from datetime import timedelta, date
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.views.generic import DeleteView, CreateView, UpdateView, ListView
# from django.contrib import messages
# from .models import Booking, Table
# from .forms import BookingForm


# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages
# from .models import Booking, Customer, Table
# from .forms import BookingForm

# def create_booking(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             booking = form.save(commit=False)
#             booking.customer_name = Customer.objects.get(pk=request.POST['customer'])
#             booking.save()
#             messages.success(request, 'Booking created successfully.')
#             return redirect('booking_list.html')
#     else:
#         form = BookingForm()
#     return render(request, 'booking/create_booking.html', {'form': form})


# def booking_manager(request):
#     return render(request, 'booking_manager.html')


# def edit_booking(request, booking_id):
#     booking = get_object_or_404(Booking, id=booking_id)
#     if request.method == 'POST':
#         form = BookingForm(request.POST, instance=booking)
#         if form.is_valid():
#             booking = form.save(commit=False)
#             booking.customer_name = Customer.objects.get(pk=request.POST['customer'])
#             booking.save()
#             messages.success(request, 'Booking updated successfully.')
#             return redirect('booking_list.html')
#     else:
#         form = BookingForm(instance=booking)
#     return render(request, 'booking/edit_booking.html', {'form': form, 'booking': booking})

# def cancel_booking(request, booking_id):
#     booking = get_object_or_404(Booking, id=booking_id)
#     if request.method == 'POST':
#         booking.delete()
#         messages.success(request, 'Booking canceled successfully.')
#         return redirect('booking_list')
#     return render(request, 'booking/cancel_booking.html', {'booking': booking})

# def rebook_booking(request, booking_id):
#     old_booking = get_object_or_404(Booking, id=booking_id)
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             new_booking = form.save(commit=False)
#             new_booking.customer_name = old_booking.customer_name
#             new_booking.save()
#             old_booking.delete()
#             messages.success(request, 'Booking rebooked successfully.')
#             return redirect('booking_list.html')
#     else:
#         form = BookingForm()
#     return render(request, 'booking/rebook_booking.html', {'form': form, 'old_booking': old_booking})

# def booking_list(request):
#     bookings = Booking.objects.all()
#     return render(request, 'booking/booking_list.html', {'bookings': bookings})


from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView
from .models import Booking, Table, Customer
from .forms import TableAvaliableForm
#from .table_avaliable import check_available
from .table_avaliable import check_avaliable
import datetime
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
#from .forms import TableAvailableForm
from booking.models import Table, Booking
#from booking.table_available import check_available

import datetime

class TableList(ListView):
    model = Table

class BookingList(ListView):
    model = Booking

class CustomerList(ListView):
    model = Customer

class BookingView(FormView):
    form_class = TableAvaliableForm
    template_name = 'tableavaliable_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        table_list = Table.objects.filter(capacity=data['capacity'])
        avaliable_tables = []
        for table in table_list:
            if check_avaliable(table, data['reservation_date'], data['reservation_time']):
                avaliable_tables.append(table)

        if len(avaliable_tables) > 0:
            table = avaliable_tables[0]
            booking = Booking.objects.create(
                user=self.request.user,
                customer_name=data['customer_name'],
                table=table,
                #number_of_guests= number_of_guests,
                reservation_date=data['reservation_date'],
                reservation_time=data['reservation_time'],
                created_on=datetime.datetime.now()
            )
            booking.save()
            return HttpResponse(str(booking))
        else:
            return HttpResponse('This table is booked! Try another one')




class BookingView(LoginRequiredMixin, FormView):
    form_class = TableAvaliableForm
    template_name = 'tableavaliable_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        table_list = Table.objects.filter(capacity=data['capacity'])
        avaliable_tables = []

        for table in table_list:
            if check_avaliable(table, data['reservation_date'], data['reservation_time']):
                avaliable_tables.append(table)

        if avaliable_tables:
            table = avaliable_tables[0]
            booking = Booking.objects.create(
                user=self.request.user,
                customer=table.customer.user,  # Assuming the User instance is stored in the customer field
                table=table,
                reservation_date=data['reservation_date'],
                reservation_time=data['reservation_time'],
                created_on=datetime.datetime.now()
            )
            booking.save()
            return HttpResponse(str(booking))
        else:
            return HttpResponse('This table is booked! Try another one')
