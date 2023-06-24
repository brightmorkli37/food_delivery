from rest_framework import viewsets, permissions
from restaurants.models import OrderItem
from restaurants.serializers import OrderItemSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            # Admin can view all order items
            return OrderItem.objects.all()
        else:
            # Regular user can view their associated order items
            return OrderItem.objects.filter(order__customer=user)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()
