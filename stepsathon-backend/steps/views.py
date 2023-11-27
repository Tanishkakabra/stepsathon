from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from steps.serializers import EventsMiniSerialzers
from steps.utils import encrypt_user_event

from steps.models import Event

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_events(request):
    """Returns all the events registered by the user, with the encrypted ticket."""
    user = request.user
    events = user.events.all()
    if events is not None:
        final_data = []
        for event in events:
            encrypted_ticket = encrypt_user_event(user, event)
            data = EventsMiniSerialzers(data=event, context={'request': request}).data
            data['encrypted_ticket'] = encrypted_ticket
            final_data.append(data)
        return Response(data=data, status=status.HTTP_200_OK)
    return Response(data={"detail":"You do not  have any registered events"})



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_event(request, event_id):
    """Returns the event, if registered by the user, with the encrypted ticket otherwise returns the event details."""
    user = request.user
    event = user.events.filter(uuid=event_id).first()
    if event is not None:
        encrypted_ticket = encrypt_user_event(user, event)
        data = EventsMiniSerialzers(data=event, context={'request': request}).data
        data['encrypted_ticket'] = encrypted_ticket
        return Response(data=data, status=status.HTTP_200_OK)
    non_registerd_event = Event.objects.filter(uuid=event_id).first()
    if non_registerd_event is not None:
        data = EventsMiniSerialzers(data=non_registerd_event, context={'request': request}).data
        return Response(data={"event_detail" : data, 
                              "detail":"You are not registered for this event"}, status=status.HTTP_200_OK)
    return Response(data={"detail":"Event does not exist"}, status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def buy_tickets(request, event_id):
    """API endpoint to add events to the user => To buy tickets for the event."""
    user = request.user
    event = Event.objects.filter(uuid=event_id).first()
    if event is not None:
        # TODO: Add additional logic to verify payment and other stuff
        if user.events.filter(uuid=event_id).exists():
            return Response(data={"detail":"You are already registered for this event"}, status=status.HTTP_200_OK)
        user.events.add(event)
        encrypted_ticket = encrypt_user_event(user, event)
        data = EventsMiniSerialzers(data=event, context={'request': request}).data
        data['encrypted_ticket'] = encrypted_ticket
        return Response(data=data, status=status.HTTP_200_OK)

    return Response(data={"detail":"Event does not exist"}, status=status.HTTP_404_NOT_FOUND)


