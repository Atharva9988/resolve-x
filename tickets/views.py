from rest_framework.views import APIView
from rest_framework.response import Response
from tickets.models import Ticket
from tickets.serializers import TicketSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class TicketListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        tickets = Ticket.objects.filter(created_by=request.user.organizations)
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=(logged_in_user := request.user), organization=logged_in_user.organizations.first())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)