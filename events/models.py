from django.db import models
from datetime import datetime
from time import time, timezone


# Create your models here.

class Event(models.Model):
    tittle = models.CharField(max_length=64, null=True)
    description = models.TextField()
    location = models.CharField(max_length=64)
    available = models.BooleanField(default=True)
    available_from = models.DateField(null=True)
    event_time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
#     TODO: price: event za free, może price wpisywać jako Decimal
#     TODO: UUIDField: unique (uniklany do pary E-mail z eventem)
