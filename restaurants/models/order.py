import uuid
from django.db import models
from django.contrib.auth import get_user_model
from restaurants.models import MenuItem, Restaurant

User = get_user_model()


class Order(models.Model):

    ORDER_STATUS_PENDING = 'P'
    ORDER_STATUS_COMPLETED = 'C'
    ORDER_STATUS_CANCELLED = 'x'

    ORDER_STATUS_CHOICES = [
        (ORDER_STATUS_PENDING, 'Pending'),
        (ORDER_STATUS_COMPLETED, 'Completed'),
        (ORDER_STATUS_CANCELLED, 'Cancelled')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(
        max_length=1, choices=ORDER_STATUS_CHOICES, default=ORDER_STATUS_PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Order ID: {self.pk} | Customer: {self.customer}"