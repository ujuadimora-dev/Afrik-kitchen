from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.views.generic.edit import FormView, View
from django.views.generic import ListView, FormView, DeleteView, UpdateView
from .models import Table, Booking
from .forms import TableAvaliableForm
from django.urls import reverse, reverse_lazy
from booking.table_avaliable import check_avaliable
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.shortcuts import redirect
import datetime




def TableListView(request):
    model = Table
    template_name = 'table_list.html'
    context_object_name = 'tables'
    table = Table.objects.all()[0]
    table_capacities = dict(table.CAPACITY_CHOICES)
    #print('capacities=', table_capacities)

    table_values = table_capacities.values()
    print('table_values=', table_values)
    table_list = []

    for table_capacity in table_capacities:
        table = table_capacities.get(table_capacity)
        #print(table)
        table_url = reverse('booking:TableDetailView', kwargs={'capacity': table_capacity})
        print(table,  table_url)
        table_list.append((table, table_url))
    context = {
        "table_list": table_list,
    }
    #print(table_list)
    return render(request, 'table_list.html', context)



class BookingList(ListView):
    model = Booking
    template_name = 'booking_list.html'
    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Booking.objects.all()
            return booking_list
        else:
            booking_list = Booking.objects.filter(user=self.request.user)
            return booking_list


class TableDetailView(View):
    def get(self, request, *args, **kwargs):
        capacity = self.kwargs.get('capacity', None)
        form = TableAvaliableForm()
        table_list = Table.objects.filter(capacity=capacity)
        
        if len(table_list) > 0:
            table = table_list[0]
            table_capacity = dict(table.CAPACITY_CHOICES).get(table.capacity, None)
            context = {
                'table_capacity': table_capacity,
                'form': form,
            }
            return render(request, 'home_detail.html', context)
        else:
            message = "This table is already booked. Please try another one."
            booking_home_url = reverse('booking:TableListView')
            return HttpResponse(f"{message} <a href='{booking_home_url}'>Booking Home</a>")

    def post(self, request, *args, **kwargs): 
        capacity = self.kwargs.get('capacity', None)
        table_list = Table.objects.filter(capacity=capacity)
        form = TableAvaliableForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data


        avaliable_tables = []
        for table in table_list:
            if check_avaliable(table, data['reservation_date'], data['reservation_time']):
                avaliable_tables.append(table)

        
        if len(avaliable_tables) > 0:
            table = avaliable_tables[0]
            booking = Booking.objects.create(
                user=self.request.user,
                table=table,
                reservation_date=data['reservation_date'],
                reservation_time=data['reservation_time']

            )
            booking.save()
            return HttpResponse(booking)
        else:
            message = "This table is already booked. Please try another one."
            booking_home_url = reverse('booking:TableListView')
            return HttpResponse(f"{message} <a href='{booking_home_url}'>Booking Home</a>")


class BookingCreateView(FormView):
    template_name = 'create_booking.html'
    form_class = TableAvaliableForm
    #success_url = 'booking/success/' 
    success_url = reverse_lazy('booking-success')
    
    def form_valid(self, form):
        data = form.cleaned_data

        # Get the table with the specified capacity
        capacity = data['capacity']
        table = get_object_or_404(Table, capacity=capacity)

        # Check if the table is available for the given reservation date and time
        if check_avaliable(table, data['reservation_date'], data['reservation_time']):
            # Create a new booking
            booking = Booking.objects.create(
                user=self.request.user,
                table=table,
                reservation_date=data['reservation_date'],
                reservation_time=data['reservation_time']
            )
            booking.save()

            messages.success(
                self.request,
                f'Booking confirmed for {booking.user} guests'
            )
            return super().form_valid(form)
        else:
            messages.error(
                self.request,
                'The chosen table is already booked. Please try another one.'
            )
            return self.form_invalid(form)


class BookingSuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'booking_success.html')
       





""" Here is the view to manage Booking"""


class CancelBookingView(DeleteView):
    model = Booking
    success_url = reverse_lazy('booking:managebookings')  # Redirect to the booking list page

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        # Update the booking status to "Cancelled" or perform any other necessary operations
        self.object.status = "Cancelled"
        self.object.save()

        return redirect(self.get_success_url())



class DeleteBookingView(DeleteView):
    model = Booking
    success_url = reverse_lazy('booking:managebookings')  # Redirect to the booking list page
    



class EditBookingView(UpdateView):
    model = Booking
    fields = ['reservation_date', 'reservation_time', 'table']
    template_name = 'booking_edit.html'
    success_url = reverse_lazy('booking:managebookings')



