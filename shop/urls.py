from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, CommandeViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('products', ProductViewSet, basename='product')
router.register('commandes', CommandeViewSet, basename='commande')

urlpatterns = router.urls
