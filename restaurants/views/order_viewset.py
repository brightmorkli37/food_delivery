from rest_framework import viewsets, permissions
from restaurants.models import Order
from rest_framework.decorators import action
from rest_framework.response import Response
from restaurants.serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Order.objects.all()
        else:
            return Order.objects.filter(customer=user)
        
    @action(detail=True, methods=['post'])
    def fulfill(self, request, pk=None):
        order = self.get_object()
        order.sttus = True
        order.save()
        return Response({'message': 'Order completed'})
        
    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()
