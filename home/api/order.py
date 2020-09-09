from rest_framework.generics import CreateAPIView
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):

    symbol = serializers.CharField(min_length=3, max_length=6)
    side = serializers.ChoiceField(choices=['SELL', 'BUY'])
    type = serializers.ChoiceField(choices=['LIMIT'])
    time_in_force = serializers.ChoiceField(choices=['GTC', 'IOC', 'FOK'])
    quantity = serializers.IntegerField(initial=0)
    price = serializers.DecimalField(decimal_places=2, max_digits=3)
    new_order_resp_type = serializers.ChoiceField(choices=['ACK', 'RESULT', 'FULL'])


class OrderCreate(CreateAPIView):
    serializer_class = OrderSerializer

