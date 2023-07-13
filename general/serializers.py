from rest_framework import serializers
from .models import Article, Tag, GenreForUrl


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class GenreForUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenreForUrl
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
