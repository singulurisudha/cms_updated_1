from rest_framework import generics
from .models import Ticket
from rest_framework.permissions import IsAuthenticated
from .serializers import TicketSerializer

class TicketListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TicketSerializer
    queryset=Ticket.objects.all()


class TicketRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TicketSerializer
    queryset=Ticket.objects.all()

