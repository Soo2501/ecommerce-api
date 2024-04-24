from rest_framework import routers
from .views import ProductViewSet, DiscountViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'discounts', DiscountViewSet)
router.register(r'categories', CategoryViewSet)