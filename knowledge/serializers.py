from rest_framework import serializers
from .models import Knowledge
from general.serializers import TagSerializer, GenreSerializer, ArticleSerializer
from general.models import Tag, GenreForURL, Article
from drf_writable_nested import WritableNestedModelSerializer


class KnowledgeSerializerForCreateUpdate(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    genre_for_url = serializers.PrimaryKeyRelatedField(
        queryset=GenreForURL.objects.all()
    )

    class Meta:
        model = Knowledge
        fields = "__all__"

    def create(self, validated_data):
        print("validated_data", validated_data)
        article_data = validated_data.pop("article")
        tags_data = validated_data.pop("tags", [])
        genre_for_url_data = validated_data.pop("genre_for_url")
        # print("article_data", article_data)
        # print("validated_data", validated_data)
        # print("tags_data", tags_data)
        # print("genre_for_url_data", genre_for_url_data)
        knowledge = Knowledge.objects.create(**validated_data)
        print("knowledge", knowledge)
        # genre_for_url = GenreForURL.objects.create(**genre_for_url_data)
        Article.objects.create(knowledge_article=knowledge, **article_data)
        knowledge.tags.set(tags_data)
        knowledge.genre_for_url = genre_for_url_data
        knowledge.save()
        return knowledge

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
    genre_for_url = GenreSerializer()

    class Meta:
        model = Knowledge
        fields = "__all__"
