from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views.generic.edit import FormView, DeleteView, UpdateView
from django.views.generic import ListView, View
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Table, Booking
from .forms import TableAvaliableForm
from booking.table_avaliable import check_avaliable

@login_required
def TableListView(request):
    model = Table
    template_name = 'table_list.html'
    context_object_name = 'tables'
    table = Table.objects.all()[0]
    table_capacities = dict(table.CAPACITY_CHOICES)
    table_list = [(table_capacities[table_capacity], reverse('booking:TableDetailView', kwargs={'capacity': table_capacity})) for table_capacity in table_capacities]
    context = {"table_list": table_list}
    return render(request, template_name, context)

class BookingList(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking_list.html'
    context_object_name = 'booking_list'
    login_url = 'home:index'

    def get_queryset(self):
        if self.request.user.is_staff:
            return Booking.objects.all()
        else:
            return Booking.objects.filter(user=self.request.user)

class TableDetailView(View):
    def get(self, request, *args, **kwargs):
        capacity = self.kwargs.get('capacity', None)
        form = TableAvaliableForm()
        table_list = Table.objects.filter(capacity=capacity)
        if table_list.exists():
            table = table_list.first()
            table_capacity = dict(table.CAPACITY_CHOICES).get(table.capacity, None)
            context = {'table_capacity': table_capacity, 'form': form}
            return render(request, 'home_detail.html', context)
        else:
            message = " Please try another one."
            booking_home_url = reverse('booking:TableListView')
            return render(request, 'already_booked.html', {'message': message})
            # message = "This table is already booked. Please try another one."
            # booking_home_url = reverse('booking:TableListView')
            # return HttpResponse(f"{message} <a href='{booking_home_url}'>Booking Home</a>")



    def post(self, request, *args, **kwargs):
        capacity = self.kwargs.get('capacity', None)
        table_list = Table.objects.filter(capacity=capacity)
        form = TableAvaliableForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            avaliable_tables = [table for table in table_list if check_avaliable(table, data['reservation_date'], data['reservation_time'])]

            if avaliable_tables:
                table = avaliable_tables[0]
                booking = Booking.objects.create(
                    user=self.request.user,
                    table=table,
                    reservation_date=data['reservation_date'],
                    reservation_time=data['reservation_time']
                )
                message = "Thanks for your Patronage."
                booking_home_url = reverse('booking:TableListView')
                return render(request, 'booking_success.html', {'message': message})
            else:
                message = "Please try another Table."
                booking_home_url = reverse('booking:TableListView')
                return render(request, 'already_booked.html', {'message': message})

                # return HttpResponse(f"{message} <a href='{booking_home_url}'>Booking Home</a>")


class BookingCreateView(FormView):
    template_name = 'create_booking.html'
    form_class = TableAvaliableForm
    success_url = reverse_lazy('booking_success')  # Use the URL name, not template name

    def form_valid(self, form):
        data = form.cleaned_data
        capacity = data['capacity']
        table = get_object_or_404(Table, capacity=capacity)

        if check_avaliable(table, data['reservation_date'], data['reservation_time']):
            booking = Booking.objects.create(
                user=self.request.user,
                table=table,
                reservation_date=data['reservation_date'],
                reservation_time=data['reservation_time']
            )
            booking.save()
            
            messages.success(self.request, f'Booking confirmed for {booking.id} guests')
            return render(request, 'booking_success.html')  # Redirect to the booking_success view

        else:
            messages.error(self.request, ' table is already booked. Please try another one.')
            return self.form_invalid(form)


#  message = f"Booking object ({booking_id}) Booking successful."
#         return render(request, 'success.html', {'message': message})



class BookingSuccessView(View):
    template_name = 'booking_success.html'  # Specify the template name here

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class BookedAlredyView(View):
    template_name = 'already_booked.html'  # Specify the template name here

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class CancelBookingView(DeleteView):
    model = Booking
    success_message = 'Booked Table Cancell successfully.'
    success_url = reverse_lazy('booking:managebookings')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.status = "Cancelled"
        self.object.save()
        return redirect(self.get_success_url())


class DeleteBookingView(DeleteView):
    model = Booking
    success_message = 'Booked Table deleted successfully.'
    success_url = reverse_lazy('booking:managebookings')


class EditBookingView(UpdateView):
    model = Booking
    fields = ['reservation_date', 'reservation_time', 'table']
    template_name = 'booking_edit.html'
    success_message = 'Booking updated successfully.'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Booking updated successfully.')
        return super().form_valid(form)

    def get_success_url(self):
        success_message = 'Booking updated successfully.'
        return reverse_lazy('booking:managebookings')

# views.py
from django.shortcuts import render, redirect
from .models import Booking

def managebooking(request):
    # Retrieve a list of bookings (customize this query based on your needs)
    bookings = Booking.objects.all()

    context = {
        'bookings': bookings,
    }

    return render(request, 'managebookings.html', context)
