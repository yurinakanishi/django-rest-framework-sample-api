from rest_framework import serializers
from .models import LivingThings, Habitat, Species
from general.serializers import TagSerializer, GenreForUrlSerializer, ArticleSerializer
from general.models import Tag, GenreForUrl, Article


class LivingThingsSerializerForCreateUpdate(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all())
    genre_for_url = serializers.PrimaryKeyRelatedField(
        queryset=GenreForUrl.objects.all()
    )

    class Meta:
        model = LivingThings
        fields = "__all__"

    def create(self, validated_data):
        article_data = validated_data.pop("article")
        tags_data = validated_data.pop("tags", [])
        genre_for_url_data = validated_data.pop("genre_for_url")
        living_things = LivingThings.objects.create(**validated_data)
        Article.objects.create(living_things_article=living_things, **article_data)
        living_things.tags.set(tags_data)
        living_things.genre_for_url = genre_for_url_data
        living_things.save()
        return living_things

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


class LivingThingsSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivingThings
        fields = ["name", "slug", "genre_for_url"]


class LivingThingsSerializerForGet(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = TagSerializer(many=True)
    genre_for_url = GenreForUrlSerializer()

    class Meta:
        model = LivingThings
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        slug = representation.get("slug", "")
        if slug.endswith("-jp"):
            representation["slug"] = slug[:-3]
        return representation


class LivingThingsSerializerForDestroy(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = TagSerializer(many=True)
    genre_for_url = GenreForUrlSerializer()

    class Meta:
        model = LivingThings
        fields = "__all__"


class HabitatSerializerForCreateUpdate(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all())
    genre_for_url = serializers.PrimaryKeyRelatedField(
        queryset=GenreForUrl.objects.all()
    )

    class Meta:
        model = Habitat
        fields = "__all__"

    def create(self, validated_data):
        article_data = validated_data.pop("article")
        tags_data = validated_data.pop("tags", [])
        genre_for_url_data = validated_data.pop("genre_for_url")
        living_things_habitat = Habitat.objects.create(**validated_data)
        Article.objects.create(
            living_things_habitat_article=living_things_habitat, **article_data
        )
        living_things_habitat.tags.set(tags_data)
        living_things_habitat.genre_for_url = genre_for_url_data
        living_things_habitat.save()
        return living_things_habitat

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


class HabitatSerializerForGet(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = TagSerializer(many=True)
    genre_for_url = GenreForUrlSerializer()

    class Meta:
        model = Habitat
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        slug = representation.get("slug", "")
        if slug.endswith("-jp"):
            representation["slug"] = slug[:-3]
        return representation


class HabitatSerializerForDestroy(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = TagSerializer(many=True)
    genre_for_url = GenreForUrlSerializer()

    class Meta:
        model = Habitat
        fields = "__all__"


class SpeciesSerializerForCreateUpdate(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all())
    genre_for_url = serializers.PrimaryKeyRelatedField(
        queryset=GenreForUrl.objects.all()
    )

    class Meta:
        model = Species
        fields = "__all__"

    def create(self, validated_data):
        article_data = validated_data.pop("article")
        tags_data = validated_data.pop("tags", [])
        genre_for_url_data = validated_data.pop("genre_for_url")
        living_things_species = Species.objects.create(**validated_data)
        Article.objects.create(
            living_things_species_article=living_things_species, **article_data
        )
        living_things_species.tags.set(tags_data)
        living_things_species.genre_for_url = genre_for_url_data
        living_things_species.save()
        return living_things_species

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


class SpeciesSerializerForGet(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = TagSerializer(many=True)
    genre_for_url = GenreForUrlSerializer()

    class Meta:
        model = Species
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        slug = representation.get("slug", "")
        if slug.endswith("-jp"):
            representation["slug"] = slug[:-3]
        return representation


class SpeciesSerializerForDestroy(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = TagSerializer(many=True)
    genre_for_url = GenreForUrlSerializer()

    class Meta:
        model = Species
        fields = "__all__"
