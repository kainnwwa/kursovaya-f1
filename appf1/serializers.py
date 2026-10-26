from rest_framework import serializers
from .models import Product, Team, Category

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # Эти поля нужны, чтобы React получал название команды и категории, а не просто их ID
    team_name = serializers.CharField(source='team.name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'