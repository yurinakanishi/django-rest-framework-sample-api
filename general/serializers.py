from rest_framework import serializers
from .models import Article, Tag, GenreForURL


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenreForURL
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
