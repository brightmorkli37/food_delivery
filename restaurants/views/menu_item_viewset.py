from rest_framework import viewsets, permissions
from restaurants.models import MenuItem
from restaurants.serializers import MenuItemSerializer
from django_filters.rest_framework import DjangoFilterBackend


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['restaurant']
