# from django.urls import path
# from .views import create_booking, edit_booking, cancel_booking, rebook_booking, booking_list, booking_manager
# from .import views

# app_name = 'booking'

# uurlpatterns = [
#     path('create/', create_booking, name='create_booking'),
#     path('edit/<int:booking_id>/', edit_booking, name='edit_booking'),
#     path('cancel/<int:booking_id>/', cancel_booking, name='cancel_booking'),
#     path('rebook/<int:booking_id>/', rebook_booking, name='rebook_booking'),
#     path('list/', booking_list, name='booking_list'),
#     path('booking_manager/', booking_manager, name='booking_manager'),
# ]


from django.urls import path
from .views import BookingList, TableList, CustomerList

app_name = 'booking'

urlpatterns = [
    path('table_list/', TableList.as_view(), name='TableList'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('customer_list/', CustomerList.as_view(), name='CustomerList'),
    path('book', BookingView.as_view(), name='booking_view')

]
