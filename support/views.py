from rest_framework import generics
from .models import Ticket
from rest_framework.permissions import IsAuthenticated
from .serializers import TicketSerializer

class TicketListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TicketSerializer

    def get_queryset(self):
        return Ticket.objects.values('issue', 'description', 'created_at', 'updated_at', 'category')

class TicketRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TicketSerializer

    def get_queryset(self):
        return Ticket.objects.values('issue', 'description', 'created_at', 'updated_at', 'category')
