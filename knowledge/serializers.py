from rest_framework import serializers
from .models import Knowledge
from general.serializers import TagSerializer, GenreForUrlSerializer, ArticleSerializer
from general.models import Tag, GenreForUrl, Article


class KnowledgeSerializerForCreateUpdate(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    genre_for_url = serializers.PrimaryKeyRelatedField(
        queryset=GenreForUrl.objects.all()
    )

    class Meta:
        model = Knowledge
        fields = "__all__"

    def create(self, validated_data):
        article_data = validated_data.pop("article")
        tags_data = validated_data.pop("tags", [])
        genre_for_url_data = validated_data.pop("genre_for_url")
        instance = Knowledge.objects.create(**validated_data)
        Article.objects.create(knowledge_article=instance, **article_data)
        instance.tags.set(tags_data)
        instance.genre_for_url = genre_for_url_data
        instance.save()
        return instance

    def update(self, instance, validated_data):
        article_data = validated_data.pop("article")
        tags_data = validated_data.pop("tags", [])
        genre_for_url_data = validated_data.pop("genre_for_url")

        instance = super().update(instance, validated_data)

        article = instance.article
        Article.objects.filter(id=article.id).update(**article_data)

        instance.tags.clear()
        instance.tags.set(tags_data)

        instance.genre_for_url = genre_for_url_data
        instance.save()

        return instance


class KnowledgeSerializerForGet(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = TagSerializer(many=True)
    genre_for_url = GenreForUrlSerializer()

    class Meta:
        model = Knowledge
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        slug = representation.get("slug", "")
        if slug.endswith("-jp"):
            representation["slug"] = slug[:-3]
        return representation


class KnowledgeSerializerForDestroy(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = TagSerializer(many=True)
    genre_for_url = GenreForUrlSerializer()

    class Meta:
        model = Knowledge
        fields = "__all__"
