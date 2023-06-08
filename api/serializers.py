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
            "slug",
            "title",
            "title_jp",
            "excerpt",
            "excerpt_jp",
            "notesite_url",
            "author",
            "published_date",
            "updated_date",
            "tags",
            "genres",
            "content",
            "content_jp",
        ]
