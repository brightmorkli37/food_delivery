from rest_framework import serializers
from restaurants.serializers import MenuItemSerializer
from restaurants.models import OrderItem, MenuItem, Order

class OrderItemSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.resolver_match:
            order_id = request.resolver_match.kwargs.get('order_id')
            if order_id:
                try:
                    order = Order.objects.get(pk=order_id)
                    self.fields['menu_item'].queryset = MenuItem.objects.filter(restaurant=order.restaurant)
                except Order.DoesNotExist:
                    pass

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            fields['order'].queryset = Order.objects.filter(customer=request.user)
        return fields
    
    menu_item = serializers.PrimaryKeyRelatedField(queryset=MenuItem.objects.all())
    # order = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'menu_item', 'quantity', 'created_at']
        read_only_fields = ['created_at',]

    def validate(self, attrs):
        order = attrs.get('order')
        menu_item = attrs.get('menu_item')

        if order and menu_item:
            if order.restaurant != menu_item.restaurant:
                raise serializers.ValidationError("Menu item does not belong to the same restaurant as the order.")

        return attrs
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['menu_item'] = instance.menu_item.name
        return representation
    
