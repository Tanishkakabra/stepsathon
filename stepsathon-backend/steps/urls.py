from django.urls import path
from steps.views import get_events, buy_tickets, get_event

urlpatterns = [
    path('api/buy-ticket/<str:event_id>/', buy_tickets, name='buy_ticket'),
    path('api/event/<str:event_id>', get_event, name='view_tickets'),
    path('api/events/', get_events, name='get_events')
]
