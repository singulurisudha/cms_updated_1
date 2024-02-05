from django.urls import path
from .views import CategoryCreateAPIView, CategoryUpdateDestroyAPIView
from .views import ContentCreateAPIView, ContenUpdateDestroyAPIView

urlpatterns = [
    path('categories/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('categories/<int:pk>/', CategoryUpdateDestroyAPIView.as_view(), name='category-update-destroy'),
    path('contents/', ContentCreateAPIView.as_view(), name='content-create'),
    path('contents/<int:pk>/',  ContenUpdateDestroyAPIView.as_view(), name='content-update-destroy'),
]
