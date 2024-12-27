from rest_framework.viewsets import ModelViewSet
from .models import Category, Product, Commande
from .serializers import CategorySerializer, ProductSerializer, CommandeSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CommandeViewSet(ModelViewSet):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
