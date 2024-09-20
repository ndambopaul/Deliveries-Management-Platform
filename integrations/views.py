from django.shortcuts import render
import json
from rest_framework.response import Response
from rest_framework import generics, status

from integrations.serializers import OrderAPICollectionSerializer
from apps.clients.models import Client, Order, OrderStatusUpdate
# Create your views here.
class OrderAPICollectionAPIView(generics.CreateAPIView):
    serializer_class = OrderAPICollectionSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid(raise_exception=True):
            client_uuid = serializer.validated_data.get("client_uuid")
            client = Client.objects.get(client_uuid=client_uuid)
            print(client.name)

            #new_data = json.loads(data)
            data.pop("client_uuid")
        
            order = Order.objects.create(
                tenant=client.tenant,
                client=client,
                **data
            )
            OrderStatusUpdate.objects.create(
                order=order,
                previous_status="Created",
                next_status="Pending Dispatch"
            )
            
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)