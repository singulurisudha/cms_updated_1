from django.urls import path
from .views import CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView
from .views import ContentListCreateAPIView, ContentRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-update-destroy'),
    path('contents/', ContentListCreateAPIView.as_view(), name='content-list-create'),
    path('contents/<int:pk>/', ContentRetrieveUpdateDestroyAPIView.as_view(), name='content-retrieve-update-destroy'),
]
