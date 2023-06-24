from rest_framework import serializers
from restaurants.models import MenuItem, Restaurant
from restaurants.serializers import RestaurantSerializer


class MenuItemSerializer(serializers.ModelSerializer):
    restaurant = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Restaurant.objects.all()
    )
    class Meta:
        model = MenuItem
        fields = [
            'id', 'name', 'description', 'price', 'restaurant', 'created_at'
        ]
        read_only_fields = ['created_at',]