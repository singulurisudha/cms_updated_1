from django.urls import path
from user.views import (UserRegistrationView , UserLoginView, UserRoleView,
                         UserModuleView, UserPermissionsView)
from django.urls import path


urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='signup'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('login/refresh/',UserLoginView.as_view(),name='refresh'),

    path('roles/', UserRoleView.as_view(), name='role-list'),
    path('roles/<int:pk>/', UserRoleView.as_view(), name='role-detail'),

    path('modules/', UserModuleView.as_view(), name='module-list'),
    path('modules/<int:pk>/', UserModuleView.as_view(), name='module-detail'),

    path('permissions/', UserPermissionsView.as_view(), name='permissions-list'),

]