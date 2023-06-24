from rest_framework import routers
from restaurants.views import (
    RestaurantViewSet, MenuItemViewSet, OrderViewSet, OrderItemViewSet
)

router = routers.DefaultRouter()

router.register('restaurants', RestaurantViewSet, basename='restaurant')
router.register('menus', MenuItemViewSet, basename='menus')
router.register('orders', OrderViewSet, basename='orders')
router.register('order_items', OrderItemViewSet, basename='order_items')


urlpatterns = router.urls


