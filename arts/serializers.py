from rest_framework import serializers
from .models import Art, Museum, PaintingMethod, PaintingStyle, Artist
from dates.models import Period
from general.serializers import TagSerializer, GenreSerializer, ArticleSerializer


class ArtSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Art
        fields = "__all__"


class MuseumSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Museum
        fields = "__all__"


class PaintingMethodSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = PaintingMethod
        fields = "__all__"


class PaintingStyleSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = PaintingStyle
        fields = "__all__"


class ArtistSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = "__all__"
