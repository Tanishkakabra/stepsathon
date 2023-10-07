from django.urls import path
from . import views

urlpatterns = [
    path('buy-ticket/<int:event_id>/', views.BuyTicket.as_view(), name='buy_ticket'),
    path('view-tickets/', views.view_tickets, name='view_tickets'),
]
