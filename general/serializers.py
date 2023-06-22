from rest_framework import serializers
from .models import Article, Tag, Genre


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            "references",
            "references_jp",
            "content",
            "content_jp",
            "rating",
            "rating_count",
        ]
