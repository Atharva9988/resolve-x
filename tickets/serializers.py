from rest_framework import serializers
from tickets.models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'created_by', 'updated_at')