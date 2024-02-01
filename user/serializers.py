from rest_framework import serializers
from .models import User , Role, Permission, Module
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password=serializers.CharField(max_length=120)
    class Meta:
        model = User
        fields = ["email", "password","mobile_number","confirm_password"]

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            mobile_number=validated_data["mobile_number"],
            password=validated_data["password"],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
class UserRoleSerializer(serializers.ModelSerializer):
    users=serializers.SerializerMethodField()
    class Meta:
        model = Role
        fields=['id','role','users']
    def get_users(self, value):
        return [user.username for user in value.users.all()]if value.users.exists() else []

class UserModuleSerializer(serializers.ModelSerializer):
    created_by=serializers.CharField(max_length=120,read_only=True)
    class Meta:
        
        model = Module
        fields = ['name', 'is_active', 'created_at', 'updated_at','created_by']
        read_only_fields = ['created_at', 'updated_at']

    def get_created_by(self, obj):
        if obj.created_by:
            return obj.created_by.username
        return None

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name cannot be empty.")
        return value
    
class UserPermissionSerializer(serializers.ModelSerializer):
    modules = serializers.SerializerMethodField()
    roles = serializers.SerializerMethodField()

    class Meta:
        model = Permission
        fields = ['modules', 'roles']
    
    def get_modules(self, obj):
        return [module.name for module in obj.modules.all()]

    def get_roles(self, obj):
        return [role.role for role in obj.roles.all()]