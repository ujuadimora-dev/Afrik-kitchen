from django.shortcuts import render, HttpResponse
from django.views.generic.edit import FormView, View
from django.views.generic import ListView, FormView
from .models import Table, Booking
from .forms import TableAvaliableForm
from django.urls import reverse
from booking.table_avaliable import check_avaliable
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

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
            return HttpResponse('This capacity of table have bben booked ')


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
            return HttpResponse('These choice of Table are booked try Another one! ')



class BookingCreateView(FormView):
    template_name = 'create_booking.html'
    form_class = TableAvaliableForm
    success_url = '/booking/success/'  # Update with the appropriate URL for successful booking
    
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

            return super().form_valid(form)
        else:
            return HttpResponse('The chosen table is already booked. Please try another one.')

class BookingSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Booking created successfully!')

