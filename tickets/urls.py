from django.urls import path
from tickets.views import TicketListView

urlpatterns = [
    path('tickets/', TicketListView.as_view(), name='ticket-list'),]