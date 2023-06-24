from django.contrib import admin
from restaurants.models import (
    Restaurant, MenuItem, Order, OrderItem
)

admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
