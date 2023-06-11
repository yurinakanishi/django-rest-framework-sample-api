from rest_framework import serializers
from .models import Art, Museum, PaintingMethod, PaintingStyle, Artist


class ArtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Art
        fields = "__all__"


class MuseumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Museum
        fields = "__all__"


class PaintingMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaintingMethod
        fields = "__all__"


class PaintingStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaintingStyle
        fields = "__all__"


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"
