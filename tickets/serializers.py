from rest_framework import serializers
from tickets.models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id','title','description','status','priority','organization','created_by','assigned_to','created_at','updated_at',)
        read_only_fields = ('id', 'created_at', 'created_by', 'updated_at', 'organization')