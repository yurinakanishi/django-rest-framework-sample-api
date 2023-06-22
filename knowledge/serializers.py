from rest_framework import serializers
from .models import Knowledge
from general.serializers import TagSerializer, GenreSerializer, ArticleSerializer


class KnowledgeSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Knowledge
        fields = "__all__"
