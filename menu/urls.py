# urls.py
from django.urls import path
from .views import MenuItemCreateAPIView, MenuItemUpdateDestroyAPIView

urlpatterns = [
    path('menu-items/', MenuItemCreateAPIView.as_view(), name='menu-create'),
    path('menu-items/<int:pk>/', MenuItemUpdateDestroyAPIView.as_view(), name='menu-item-update-delete'),
]
