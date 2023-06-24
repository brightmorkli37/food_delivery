import uuid
from django.db import models
from django.core.validators import MinValueValidator
from restaurants.models import Restaurant


class MenuItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, validators=[MinValueValidator(1)]
    )
    description = models.TextField(blank=True, null=True)   

    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='menu_items'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name