from django.shortcuts import render, HttpResponse
from django.views.generic.edit import FormView
from django.views.generic import ListView, FormView
from .models import Table, Booking, Customer
from .forms import TableAvaliableForm
from booking.table_avaliable import check_avaliable
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

import datetime



class TableList(ListView):
    model = Table


class CustomerList(ListView):
    model = Customer


class BookingList(ListView):
    model = Booking



    

# class BookingView(FormView):
#     form_class = TableAvaliableForm
#     template_name = 'tableavaliable_form.html'
#     #success_url = '/success/'  # Replace with your desired success URL

#     def form_valid(self, form):
#         data = form.cleaned_data
#         table_num = data['table_num']
#         reservation_date = data['reservation_date']
#         reservation_time = data['reservation_time']

#         table = Table.objects.filter(table_number=table_num).first()
#         if table:
#             if check_avaliable(table, reservation_date, reservation_time):
#                 booking = Booking.objects.create(
#                     customer=self.request.customer,
#                     table=table,
#                     reservation_date=reservation_date,
#                     reservation_time=reservation_time
#                 )
#                 booking.save()
#                 return super().form_valid(form)
#             else:
#                 return HttpResponse('This table is already booked! Please choose another one.')

#         return HttpResponse('Invalid table number!')

#     def get_success_url(self):
#         return self.success_url



                
# #from django.contrib.auth import get_user_model

# class BookingView(FormView):
#     form_class = TableAvaliableForm
#     template_name = 'tableavaliable_form.html'

#     def form_valid(self, form):
#         data = form.cleaned_data
#         table_list = Table.objects.filter(table_number=data['table_num'])
#         avaliable_tables = []
        
#         #User = get_user_model()  # Get the User model

#         for table in table_list:
#             if check_avaliable(table, data['reservation_date'], data['reservation_time']):
#                 avaliable_tables.append(table)

#         if len(avaliable_tables) > 0:
#             table = avaliable_tables[0]
            
#             # Create the booking instance
#             customer = customer.objects.get(username=data['customer_name'])  # Assuming 'customer_name' is a valid field
#             booking = Booking.objects.create(
#                 customer=customer,
#                 table=table,
#                 reservation_date=data['reservation_date'],
#                 reservation_time=data['reservation_time']
#             )
#             return HttpResponse(str(booking))  # Return the booking instance
#         else:
# #             return HttpResponse('This table number is already booked! Try another one')


# from django.contrib.auth import get_user_model

# class BookingView(FormView):
#     form_class = TableAvaliableForm
#     template_name = 'tableavaliable_form.html'

#     def form_valid(self, form):
#         data = form.cleaned_data
#         table_list = Table.objects.filter(table_number=data['table_num'])
#         avaliable_tables = []
        
#         User = get_user_model()  # Get the User model

#         for table in table_list:
#             if check_avaliable(table, data['reservation_date'], data['reservation_time']):
#                 avaliable_tables.append(table)

#         if len(avaliable_tables) > 0:
#             table = avaliable_tables[0]
            
#             # Create the booking instance
#             customer = User.objects.get(username=data['customer_name'])  # Assuming 'customer_name' is a valid field
#             booking = Booking.objects.create(
#                 customer=customer,
#                 table=table,
#                 reservation_date=data['reservation_date'],
#                 reservation_time=data['reservation_time']
#             )
#             return HttpResponse(str(booking))  # Return the booking instance
#         else:
#             return HttpResponse('This table number is already booked! Try another one')

#         return super().form_valid(form)  # Add this line to handle the case when there are no avaliable tables

# def form_valid(self, form):
#     data = form.cleaned_data
#     table_list = Table.objects.filter(table_number=data['table_num'])
#     avaliable_tables = []
    
#     for table in table_list:
#         if check_avaliable(table, data['reservation_date'], data['reservation_time']):
#             avaliable_tables.append(table)

#     if len(avaliable_tables) > 0:
#         table = avaliable_tables[0]
#         customer_name = data.get('customer_name')  # Safely retrieve the value using get()
        
#         if customer:
#             booking = Booking.objects.create(
#                 customer=customer,  # Use the correct field name
#                 table=table,
#                 reservation_date=data['reservation_date'],
#                 reservation_time=data['reservation_time']
#             )
#             booking.save()
#             return HttpResponse(str(booking))
#         else:
#             return HttpResponse('Please provide a valid customer name.')
#     else:
#         return HttpResponse('This table number is already booked! Try another one.')



# from django.shortcuts import HttpResponse
# from django.contrib.auth import get_user_model
# from django.views.generic.edit import FormView
# from .forms import TableAvaliableForm
# from .models import Table, Booking

# class BookingView(FormView):
#     form_class = TableAvaliableForm
#     template_name = 'tableavaliable_form.html'

#     def form_valid(self, form):
#         data = form.cleaned_data
#         table_list = Table.objects.filter(table_number=data['table_num'])
#         avaliable_tables = []
        
#         for table in table_list:
#             if check_avaliable(table, data['reservation_date'], data['reservation_time']):
#                 avaliable_tables.append(table)

#         if len(avaliable_tables) > 0:
#             table = avaliable_tables[0]
#             customer_name = data.get('customer_name')  # Safely retrieve the value using get()
            
#             if customer_name:
#                 User = get_user_model()
#                 customer = User.objects.get(username=customer_name)
                
#                 booking = Booking.objects.create(
#                     customer=customer,
#                     table=table,
#                     reservation_date=data['reservation_date'],
#                     reservation_time=data['reservation_time']
#                 )
#                 booking.save()
#                 return HttpResponse(str(booking))
#             else:
#                 return HttpResponse('Please provide a valid customer name.')
#         else:
#             return HttpResponse('This table number is already booked! Try another one.')




# class BookingView(FormView):
#     form_class = TableAvaliableForm
#     template_name = 'tableavaliable_form.html'

#     def form_valid(self, form):
#         data = form.cleaned_data
#         table_list = Table.objects.filter(table_number=data['table_num'])
#         avaliable_tables = []

#         for table in table_list:
#             if check_avaliable(table, data['reservation_date'], data['reservation_time']):
#                 avaliable_tables.append(table)

#         if len(avaliable_tables) > 0:
#             table = avaliable_tables[0]
#             customer_name = data.get('customer_name')  # Safely retrieve the value using get()

#             if customer_name:
#                 try:
#                     customer = get_user_model().objects.get(username=customer_name)
#                 except ObjectDoesNotExist:
#                     return HttpResponse('User does not exist. Please provide a valid customer name.')

#                 booking = Booking.objects.create(
#                     customer=customer,
#                     table=table,
#                     reservation_date=data['reservation_date'],
#                     reservation_time=data['reservation_time']
#                 )
#                 booking.save()
#                 return HttpResponse(booking)
#             else:
#                 return HttpResponse('Please provide a valid customer name.')
#         else:
#             return HttpResponse('This table number is already booked! Try another one.')



# from django.core.exceptions import ObjectDoesNotExist

# class BookingView(FormView):
#     form_class = TableAvaliableForm
#     template_name = 'tableavaliable_form.html'

#     def form_valid(self, form):
#         data = form.cleaned_data
#         table_list = Table.objects.filter(table_number=data['table_num'])
#         avaliable_tables = []

#         for table in table_list:
#             if check_avaliable(table, data['reservation_date'], data['reservation_time']):
#                 avaliable_tables.append(table)

#         if len(avaliable_tables) > 0:
#             table = avaliable_tables[0]
#             customer_name = data.get('customer_name')  # Safely retrieve the value using get()

#             if customer_name:
#                 try:
#                     customer = get_user_model().objects.get(username=customer_name)
#                 except ObjectDoesNotExist:
#                     return HttpResponse('User does not exist. Please provide a valid customer name.')

#                 booking = Booking.objects.create(
#                     customer=customer,
#                     table=table,
#                     reservation_date=data['reservation_date'],
#                     reservation_time=data['reservation_time']
#                 )
#                 return HttpResponse(str(booking))
#             else:
#                 return HttpResponse('Please provide a valid customer name.')
#         else:
#             return HttpResponse('This table number is already booked! Try another one.')



from django.shortcuts import HttpResponse
from django.contrib.auth import get_user_model
from django.views.generic.edit import FormView
from .forms import TableAvaliableForm
from .models import Table, Booking

class BookingView(FormView):
    form_class = TableAvaliableForm
    template_name = 'tableavaliable_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        table_list = Table.objects.filter(table_number=data['table_num'])
        avaliable_tables = []
        
        for table in table_list:
            if check_avaliable(table, data['reservation_date'], data['reservation_time']):
                avaliable_tables.append(table)

        if len(avaliable_tables) > 0:
            table = avaliable_tables[0]
            customer_name = data.get('customer_name')  # Safely retrieve the value using get()
            
            if customer_name:
                User = get_user_model()
                customer = User.objects.get(username=customer_name)
                
                booking = Booking.objects.create(
                    customer=customer,
                    table=table,
                    reservation_date=data['reservation_date'],
                    reservation_time=data['reservation_time']
                )
                booking.save()
                return HttpResponse(str(booking))
            else:
                return HttpResponse('Please provide a valid customer name.')
        else:
            return HttpResponse('This table number is already booked! Try another one.')
