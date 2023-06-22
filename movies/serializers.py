from rest_framework import serializers
from .models import Movie, MovieActor, MovieRating, MovieDirector, MovieReview
from general.serializers import TagSerializer, GenreSerializer, ArticleSerializer


class MovieRatingSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = MovieRating
        fields = "__all__"


class MovieReviewSerializer(serializers.ModelSerializer):
    rating = MovieRatingSerializer(read_only=True)
    article = ArticleSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = MovieReview
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"


class MovieActorSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = MovieActor
        fields = "__all__"
