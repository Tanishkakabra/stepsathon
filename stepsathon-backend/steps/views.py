from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Event, Ticket
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .utils import generate_qr_code





@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_tickets(request):
    user_tickets = Ticket.objects.filter(user=request.user)

    # Serialize the user's tickets into a JSON format
    ticket_data = [{'event_name': ticket.event.name, 'ticket_number': str(ticket.unique_ticket_number)} for ticket in user_tickets]

    return Response({'tickets': ticket_data})


class BuyTicket(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)

        # Create a new ticket for the user
        ticket = Ticket(event=event, user=request.user)
        ticket.save()

        return Response({'message': 'Ticket purchased successfully'}, status=status.HTTP_201_CREATED)
