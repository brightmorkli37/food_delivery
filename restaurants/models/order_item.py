import uuid
from django.db import models
from django.core.exceptions import ValidationError
from restaurants.models import Order, MenuItem


class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.menu_item}| Quantity: ({self.quantity})"
    
    def clean(self):
        if self.order.restaurant != self.menu_item.restaurant:
            raise ValidationError("Menu item does not belong to the same restaurant as the order.")