from rest_framework import serializers
from .models import Food, CookingMethod, Ingredient
from general.serializers import TagSerializer, GenreSerializer, ArticleSerializer


class FoodSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=False)
    tags = TagSerializer(many=True, read_only=False)
    genre_for_url = GenreSerializer(many=True, read_only=False)

    class Meta:
        model = Food
        fields = "__all__"


class CookingMethodSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=False)
    tags = TagSerializer(many=True, read_only=False)
    genre_for_url = GenreSerializer(many=True, read_only=False)

    class Meta:
        model = CookingMethod
        fields = "__all__"


class IngredientsSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=False)
    tags = TagSerializer(many=True, read_only=False)
    genre_for_url = GenreSerializer(many=True, read_only=False)

    class Meta:
        model = Ingredient
        fields = "__all__"
