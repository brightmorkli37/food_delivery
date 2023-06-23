from rest_framework import routers
from restaurants.views import RestaurantViewSet

router = routers.DefaultRouter()

router.register('restaurants', RestaurantViewSet, basename='restaurant')


urlpatterns = router.urls


