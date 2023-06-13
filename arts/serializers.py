from rest_framework import serializers
from .models import Art, Museum, ArtMethod, ArtStyle, Artist
from dates.models import Period


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
        model = ArtMethod
        fields = "__all__"


class PaintingStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtStyle
        fields = "__all__"


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"


class ArtPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = "__all__"
