from django.urls import path
from .views import BookingList, TableListView, TableDetailView

app_name = 'booking'

urlpatterns = [
    path('table_list/', TableListView, name='TableListView'),
    path('booking_list/', BookingList.as_view(), name='BookingListView'),
    #path('customer_list/', CustomerList.as_view(), name='CustomerList'),
    #path('book/', BookingView.as_view(), name='bookingview'),
    path('table/<capacity>', TableDetailView.as_view(), name='TableDetailView')

]
