from rest_framework import routers
from restaurants.views import (
    RestaurantViewSet, MenuItemViewSet
)

router = routers.DefaultRouter()

router.register('restaurants', RestaurantViewSet, basename='restaurant')
router.register('menus', MenuItemViewSet, basename='menus')


urlpatterns = router.urls


