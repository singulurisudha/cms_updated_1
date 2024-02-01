# serializers.py
from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(max_length=120)
    class Meta:
        model = Ticket
        fields = ['id', 'issue', 'description', 'created_at', 'updated_at', 'status','created_by']  # Renamed 'title' to 'issue'

    def create(self, validated_data):

        return Ticket.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.issue = validated_data.get('issue', instance.issue)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
