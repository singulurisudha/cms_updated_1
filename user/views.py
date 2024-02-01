from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import (UserRegistrationSerializer , UserLoginSerializer ,
                UserRoleSerializer,UserModuleSerializer, UserPermissionSerializer)
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import User , Role , Permission, Module
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "Successfully Created"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            
            # Use authenticate to check email and password
            user = authenticate(request, email=email, password=password)

            if User is not None:
                refresh = RefreshToken.for_user(User)
                return Response({
                    'tokens': {
                        'access': str(refresh.access_token),
                        'refresh': str(refresh)
                    }
                }, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRoleView(APIView):
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            try:
                role = Role.objects.get(pk=pk)
                serializer = UserRoleSerializer(role)
                return Response(serializer.data)
            except Role.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            roles = Role.objects.all()
            serializer = UserRoleSerializer(roles, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = UserRoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, *args, **kwargs):
        try:
            role = Role.objects.get(pk=pk)
            serializer = UserRoleSerializer(role, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Role.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, *args, **kwargs):
        try:
            role = Role.objects.get(pk=pk)
            role.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Role.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class UserPermissionsView(APIView):
    def get(self, request, pk=None):
        if pk:
            permission = Permission.objects.filter(pk=pk).first()
            if not permission:
                return Response({"error": "Permission not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = UserPermissionSerializer(permission)
            return Response(serializer.data)
        else:
            permissions = Permission.objects.all()
            serializer = UserPermissionSerializer(permissions, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = UserPermissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        permission = Permission.objects.filter(pk=pk).first()
        if not permission:
            return Response({"error": "Permission not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserPermissionSerializer(permission, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        permission = Permission.objects.filter(pk=pk).first()
        if not permission:
            return Response({"error": "Permission not found"}, status=status.HTTP_404_NOT_FOUND)
        permission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserModuleView(APIView):
    def get(self, request, pk=None):
        if pk:
            module = get_object_or_404(Module, pk=pk)
            serializer = UserModuleSerializer(module)
            return Response(serializer.data)
        else:
            modules = Module.objects.all()
            serializer = UserModuleSerializer(modules, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = UserModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        module = get_object_or_404(Module, pk=pk)
        serializer = UserModuleSerializer(module, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        module = get_object_or_404(Module, pk=pk)
        module.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)