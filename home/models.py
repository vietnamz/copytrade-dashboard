from django.db import models
from django.contrib.auth.models import User


class TimeInForce(models.Model):
    symbol = models.CharField(max_length=6, help_text='GTK, IOC, or FOK', unique=True)
    name = models.CharField(max_length=255, help_text='The human readable text')


class OrderType(models.Model):
    symbol = models.CharField(max_length=25, help_text='The symbol of the order type', unique=True)
    name = models.CharField(max_length=255, help_text='The human readable text')


class OrderSideType(models.Model):
    symbol = models.CharField(max_length=15, help_text='The symbol of the type', unique=True)
    name = models.CharField(max_length=255, help_text='The human readable text')


class Order(models.Model):
    """
    Model representing a order.
    """
    symbol = models.CharField(name='symbol', max_length=8,
                              help_text="The symbol to be fill. etc... BTCUSD",
                              null=False)

    type = models.ForeignKey(OrderType, default=1, on_delete=models.PROTECT)

    side = models.ForeignKey(OrderSideType, default=1, on_delete=models.CASCADE)

    time_in_force = models.ForeignKey(TimeInForce, default=1, on_delete=models.SET_NULL, null=True)

