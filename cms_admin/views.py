from django.shortcuts import render
from rest_framework import generics
from menu.models import MenuItem
from support.views import *
from menu.serializers import MenuItemSerializer
from category.views import *

class MenuItemListAPIView(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuItemRetrieveAPIView(generics.RetrieveAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ContentListAPIView(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ContentRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def get_queryset(self):
        # Get the logged-in user
        user = self.request.user
        
        # Check if the user is archived
        if user:
            # If the user is archived, return an empty queryset
             return Content.objects.filter(created_by=user)
        else:
            # If the user is not archived, return the queryset of non-archived content
            return Content.objects.all()

    

class SupportListAPIView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class SupportRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

