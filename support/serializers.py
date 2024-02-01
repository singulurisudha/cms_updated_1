# serializers.py
from rest_framework import serializers
from .models import Ticket
from rest_framework.permissions import IsAuthenticated

    
class TicketSerializer(serializers.ModelSerializer):
    created_by=serializers.CharField(max_length=120,read_only=True)
    class Meta:
        model = Ticket
        fields = ['id', 'issue', 'description', 'created_at', 'updated_at', 'status', 'created_by']

    # Add the permission_classes attribute to specify permissions for the serializer
    permission_classes = [IsAuthenticated]
    
    def get_created_by(self,obj):
        if obj:
            obj.created_by.username

    def create(self, validated_data):
        # Check if the user is authenticated before creating the ticket
        if self.context['request'].user.is_authenticated:
            validated_data['created_by'] = self.context['request'].user
            return Ticket.objects.create(**validated_data)
        else:
            raise serializers.ValidationError("User must be authenticated to create a ticket.")

    def update(self, instance, validated_data):
        # Check if the user is authenticated before updating the ticket
        if self.context['request'].user.is_authenticated:
            instance.issue = validated_data.get('issue', instance.issue)
            instance.description = validated_data.get('description', instance.description)
            instance.save()
            return instance
        else:
            raise serializers.ValidationError("User must be authenticated to update a ticket.")