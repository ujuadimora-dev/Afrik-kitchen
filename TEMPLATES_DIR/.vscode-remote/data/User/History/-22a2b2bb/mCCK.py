from django import forms
from .models import Booking, Table, Customer

class TableAvaliableForm(forms.Form):
    CAPACITY_CHOICES = (
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (8, "8"),
        (14, "14"),
        (20, "20"),
    )

    TABLE_POSITION = (
        ("window", "Tables near the window"),
        ("middle", "Tables in the middle"),
        ("outside", "Tables outside in the garden"),
        ("corridor", "Tables on the corridor"),
    )

    BOOKING_TIME = (
        (1, "8:00am - 9:45am"),
        (2, "10:00am - 12:45pm"),
        (3, "1:00pm - 2:45pm"),
        (4, "3:00pm - 5:45pm"),
        (5, "7:00pm - 8:45pm"),
    )

    customer_name = forms.CharField(max_length=100, required=True)
    capacity = forms.ChoiceField(choices=CAPACITY_CHOICES, required=True)
    reservation_date = forms.DateField(
        label='Reservation Date',
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=["%Y-%m-%d"],
        required=True
    )
    reservation_time = forms.ChoiceField(
        choices=BOOKING_TIME,
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    table_position = forms.ChoiceField(
        choices=TABLE_POSITION,
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    table_number = forms.IntegerField(required=True)

    def clean_table_number(self):
        table_number = self.cleaned_data.get('table_number')
        if table_number is not None:
            try:
                table = Table.objects.get(table_number=table_number)
                if table.status != 'available':
                    raise forms.ValidationError("The selected table is not available. Please choose another table.")
            except Table.DoesNotExist:
                raise forms.ValidationError("Invalid table number. Please choose a valid table number.")
        return table_number

    def clean(self):
        cleaned_data = super().clean()
        capacity = cleaned_data.get('capacity')
        table_position = cleaned_data.get('table_position')

        if capacity and table_position:
            table_num = self.get_table_number(capacity)
            table = Table.objects.filter(table_number=table_num, position=table_position).first()
            

            if not table:
                raise forms.ValidationError("No table available with the selected capacity and position.")

        return cleaned_data

    def get_table_number(self, capacity):
        capacity_table_mapping = {
            2: 2,
            3: 3,
            4: 4,
            8: 8,
            14: 14,
            20: 20,
        }

        return capacity_table_mapping.get(int(capacity))

    def save(self, user, customer_name):
        capacity = self.cleaned_data['capacity']
        table_position = self.cleaned_data['table_position']
        booking_time = self.cleaned_data['reservation_time']

        table_num = self.get_table_number(capacity)
        table = Table.objects.get(table_num=table_num, table_position=table_position)

        customer = Customer.objects.create(name=customer_name)
        booking = Booking.objects.create(
            user=user,
            customer=customer,
            table=table,
            reservation_date=self.cleaned_data['reservation_date'],
            reservation_time=booking_time,
            created_on=datetime.datetime.now()
        )
        return booking
