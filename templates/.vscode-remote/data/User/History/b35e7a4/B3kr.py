from django import forms
from .models import Booking, Table, Customer

# class TableAvaliableForm(forms.Form):
#     CAPACITY_CHOICES = (
#         (2, "2"),
#         (3, "3"),
#         (4, "4"),
#         (8, "8"),
#         (14, "14"),
#         (20, "20"),
#     )

#     TABLE_POSITION = (
#         ("window", "Tables near the window"),
#         ("middle", "Tables in the middle"),
#         ("outside", "Tables outside in the garden"),
#         ("corridor", "Tables on the corridor"),
#     )

#     BOOKING_TIME = (
#         (1, "8:00am - 9:45am"),
#         (2, "10:00am - 12:45pm"),
#         (3, "1:00pm - 2:45pm"),
#         (4, "3:00pm - 5:45pm"),
#         (5, "7:00pm - 8:45pm"),
#     )

#     customer_name = forms.CharField(max_length=100, required=True)
#     capacity = forms.ChoiceField(choices=CAPACITY_CHOICES, required=True)
#     reservation_date = forms.DateField(
#         label='Reservation Date',
#         widget=forms.DateInput(attrs={'type': 'date'}),
#         input_formats=["%Y-%m-%d"],
#         required=True
#     )
#     reservation_time = forms.ChoiceField(
#         choices=BOOKING_TIME,
#         required=True,
#         widget=forms.Select(attrs={'class': 'form-select'})
#     )
#     table_position = forms.ChoiceField(
#         choices=TABLE_POSITION,
#         required=True,
#         widget=forms.Select(attrs={'class': 'form-select'})
#     )
#     table_number = forms.IntegerField(required=True)

#     def clean_table_number(self):
#         table_number = self.cleaned_data.get('table_number')
#         if table_number is not None:
#             try:
#                 table = Table.objects.get(table_num=table_number)
#                 if table.status != 'avaliable':
#                     raise forms.ValidationError("The selected table is not available. Please choose another table.")
#             except Table.DoesNotExist:
#                 raise forms.ValidationError("Invalid table number. Please choose a valid table number.")
#         return table_number





# from django import forms
# from .models import Booking, Table, Customer

# class TableAvaliableForm(forms.Form):
#     CAPACITY_CHOICES = (
#         (2, "2"),
#         (3, "3"),
#         (4, "4"),
#         (8, "8"),
#         (14, "14"),
#         (20, "20"),
#     )

#     TABLE_CHOICES = (
#         (2, "2"),
#         (3, "3"),
#         (4, "4"),
#         (8, "8"),
#         (14, "14"),
#         (20, "20"),
#     )

#     TABLE_POSITION = (
#         ("window", "Tables near the window"),
#         ("middle", "Tables in the middle"),
#         ("outside", "Tables outside in the garden"),
#         ("corridor", "Tables on the corridor"),
#     )

#     BOOKING_TIME = (
#         (1, "8:00am - 9:45am"),
#         (2, "10:00am - 12:45pm"),
#         (3, "1:00pm - 2:45pm"),
#         (4, "3:00pm - 5:45pm"),
#         (5, "7:00pm - 8:45pm"),
#     )

#     customer_name = forms.CharField(max_length=100, required=True)
#     table_num = forms.ChoiceField(choices=TABLE_CHOICES, required=True)
#     capacity = forms.ChoiceField(choices=CAPACITY_CHOICES, required=True)
#     reservation_date = forms.DateField(
#         label='Reservation Date',
#         widget=forms.DateInput(attrs={'type': 'date'}),
#         input_formats=["%Y-%m-%d"],
#         required=True
#     )
#     reservation_time = forms.ChoiceField(
#         choices=BOOKING_TIME,
#         required=True,
#         widget=forms.Select(attrs={'class': 'form-select'})
#     )
#     table_position = forms.ChoiceField(
#         choices=TABLE_POSITION,
#         required=True,
#         widget=forms.Select(attrs={'class': 'form-select'})
#     )
#     table_number = forms.IntegerField(required=True)

#     def clean_table_number(self):
#         table_number = self.cleaned_data.get('table_number')
#         capacity = self.cleaned_data.get('capacity')
#         if table_number is not None:
#             try:
#                 table_num = self.get_table_number(int(capacity))
#                 table = Table.objects.get(table_num=table_num)
#                 if table.status != 'available':
#                     raise forms.ValidationError("The selected table is not available. Please choose another table.")
#             except Table.DoesNotExist:
#                 raise forms.ValidationError("Invalid table number. Please choose a valid table number.")
#         return table_number

#     @staticmethod
#     def get_table_number(capacity):
#         capacity_table_mapping = {
#             2: 4,
#             3: 3,
#             4: 2,
#             8: 8,
#             14: 14,
#             20: 20,
#         }
#         return capacity_table_mapping.get(capacity, 0)


from django import forms
from .models import Table

class TableAvaliableForm(forms.Form):
    CAPACITY_CHOICES = (
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (8, "8"),
        (14, "14"),
        (20, "20"),
    )

    TABLE_CHOICES = (
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
    wheelchair_accessibility = forms.BooleanField(initial=False)
    table_num = forms.ChoiceField(choices=TABLE_CHOICES, required=True)
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

    def clean(self):
        cleaned_data = super().clean()
        reservation_time = cleaned_data.get('reservation_time')
        if reservation_time:
            cleaned_data['reservation_time_label'] = dict(self.BOOKING_TIME).get(int(reservation_time), '')
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['table_num'].choices = self.get_table_choices()

    def get_table_choices(self):
        table_choices = []
        tables = Table.objects.all()
        for table in tables:
            table_choices.append((table.table_num, str(table.table_num)))
        return table_choices
