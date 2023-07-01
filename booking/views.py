from django.shortcuts import render, HttpResponse
from django.views.generic.edit import FormView
from django.views.generic import ListView, FormView
from .models import Table, Booking
from .forms import TableAvaliableForm
from booking.table_avaliable import check_avaliable
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

import datetime



class TableList(ListView):
    model = Table


# class CustomerList(ListView):
#     model = Customer


class BookingList(ListView):
    model = Booking




class BookingView(FormView):
    form_class = TableAvaliableForm
    template_name = 'tableavaliable_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        table_list = Table.objects.filter(capacity = data['capacity_choices'])
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



        
