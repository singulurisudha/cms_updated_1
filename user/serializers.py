from rest_framework import serializers
from django.contrib.auth.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User

        fields = ('username', 'email', 'password', 'is_staff')

        fields = ('username', 'email', 'password','is_staff')

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if validated_data.get('is_staff'):
            superuser = User.objects.create_superuser(**validated_data)
            return superuser
        else:
            user = User.objects.create_user(**validated_data)
            return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class ForgetPasswordUpdateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


