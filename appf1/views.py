from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer # <-- Импортируем наш сериализатор

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer # <-- Указываем его здесь
