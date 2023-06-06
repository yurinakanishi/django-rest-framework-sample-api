from rest_framework import serializers
from articles.models import Article, Tag, Genre


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = [
            "name",
            "title",
            "language",
            "excerpt",
            "notesite_url",
            "author",
            "date_published",
            "tags",
            "genres",
            "content",
        ]
