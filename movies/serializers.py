from rest_framework import serializers
from .models import Movie, MovieActor, MovieRating, MovieDirector
from general.serializers import TagSerializer, GenreSerializer, ArticleSerializer


class MovieSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"


class MovieActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieActor
        fields = "__all__"


class MovieRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRating
        fields = "__all__"


class MovieRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRating
        fields = "__all__"
