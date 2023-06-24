from rest_framework import serializers
from restaurants.models import Order, OrderItem, Restaurant
from restaurants.serializers import OrderItemSerializer, MenuItemSerializer


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(), read_only=True
    )
    restaurant = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())
    order_items = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'id', 'customer', 'restaurant', 'status', 'created_at', 
            'order_items', 'total_price',
        ]
        read_only_fields = ['created_at', 'status']

    def create(self, validated_data):
        validated_data['customer'] = self.context['request'].user
        restaurant = validated_data.get('restaurant')
        if not restaurant:
            raise serializers.ValidationError("Restaurant is required.")
        
        return super().create(validated_data)        

    def update(self, instance, validated_data):
        restaurant = validated_data.get('restaurant')
        if not restaurant:
            raise serializers.ValidationError("Restaurant is required.")
        return super().update(instance, validated_data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['customer'] = str(instance.customer)
        representation['restaurant'] = str(instance.restaurant)
        return representation
    
    def get_order_items(self, instance):
        order_items = instance.order_items.all()
        serializer = OrderItemSerializer(order_items, many=True)
        return serializer.data
    
    def get_total_price(self, obj):
        order_items = obj.order_items.all()
        total_price = sum(item.menu_item.price * item.quantity for item in order_items)
        return total_price