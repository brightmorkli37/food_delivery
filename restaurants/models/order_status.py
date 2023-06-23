import uuid
from django.db import models
from restaurants.models import Order



class OrderStatus(models.Model):

    ORDER_STATUS_PENDING = 'P'
    ORDER_STATUS_COMPLETED = 'C'
    ORDER_STATUS_CANCELLED = 'x'

    ORDER_STATUS_CHOICES = [
        (ORDER_STATUS_PENDING, 'Pending'),
        (ORDER_STATUS_COMPLETED, 'Completed'),
        (ORDER_STATUS_CANCELLED, 'Cancelled')
    ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE, primary_key=True)
    status = models.CharField(max_length=1, choices=ORDER_STATUS_CHOICES, default=ORDER_STATUS_PENDING)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Order: {self.order} | Status: {self.status}"