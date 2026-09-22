from .views import ProductViewSet,CartItemViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('products',ProductViewSet,basename='products')
router.register('cart',CartItemViewSet,basename='cart')
urlpatterns =router.urls