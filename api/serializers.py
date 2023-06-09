from rest_framework import serializers
from articles.models import Article, Tag, Genre, MovieRating


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class MovieRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRating
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    movie_rating = MovieRatingSerializer(read_only=True)

    class Meta:
        model = Article
        fields = [
            "slug",
            "title",
            "title_jp",
            "excerpt",
            "excerpt_jp",
            "references",
            "references_jp",
            "notesite_url",
            "author",
            "published_date",
            "updated_date",
            "tags",
            "genres",
            "content",
            "content_jp",
            "rating",
            "rating_count",
            "movie_rating",
        ]
