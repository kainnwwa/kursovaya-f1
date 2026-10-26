from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet


router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    # Подключаем все пути, созданные роутером
    path('', include(router.urls)),
]