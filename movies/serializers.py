from rest_framework import serializers
from .models import Movie, MovieActor, MovieRating, MovieDirector, MovieReview
from general.serializers import TagSerializer, GenreSerializer, ArticleSerializer


class MovieRatingSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=False)
    tags = TagSerializer(many=True, read_only=False)
    genre_for_url = GenreSerializer(many=True, read_only=False)

    class Meta:
        model = MovieRating
        fields = "__all__"


class MovieReviewSerializer(serializers.ModelSerializer):
    rating = MovieRatingSerializer(read_only=False)
    article = ArticleSerializer(read_only=False)
    tags = TagSerializer(many=True, read_only=False)
    genre_for_url = GenreSerializer(many=True, read_only=False)

    class Meta:
        model = MovieReview
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=False)
    tags = TagSerializer(many=True, read_only=False)
    genre_for_url = GenreSerializer(many=True, read_only=False)

    class Meta:
        model = Movie
        fields = "__all__"


class MovieActorSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=False)
    tags = TagSerializer(many=True, read_only=False)
    genre_for_url = GenreSerializer(many=True, read_only=False)

    class Meta:
        model = MovieActor
        fields = "__all__"
