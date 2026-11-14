from rest_framework import serializers
from tickets.models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    def validate_assigned_to(self, value):
        if value and value.organization != self.context['request'].user.organization:
            raise serializers.ValidationError("Agent must belong to the same organization.")
        return value

    class Meta:
        model = Ticket
        fields = ('id','title','description','status','priority','organization','created_by','assigned_to','created_at','updated_at',)
        read_only_fields = ('id', 'created_at', 'created_by', 'updated_at', 'organization')