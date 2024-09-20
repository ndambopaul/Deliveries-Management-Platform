from rest_framework import serializers

class OrderAPICollectionSerializer(serializers.Serializer):
    order_number = serializers.CharField(max_length=255)
    customer_name = serializers.CharField(max_length=255)
    customer_phone = serializers.CharField(max_length=255)
    delivery_cost = serializers.DecimalField(max_digits=100, decimal_places=2)
    customer_location = serializers.JSONField(default=dict)
    customer_address = serializers.CharField(max_length=500)
    client_uuid = serializers.CharField(max_length=255)
    delivery_urgency = serializers.CharField(max_length=255)
    additional_details = serializers.JSONField(default=dict)


