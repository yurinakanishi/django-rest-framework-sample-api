from rest_framework import serializers
from .models import Art, Museum, PaintingMethod, PaintingStyle, Artist, ArtsPeriod
from general.serializers import TagSerializer, GenreForUrlSerializer, ArticleSerializer
from general.models import Tag, GenreForUrl, Article


class ArtSerializerForCreateUpdate(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    genre_for_url = serializers.PrimaryKeyRelatedField(
        queryset=GenreForUrl.objects.all()
    )

    class Meta:
        model = Art
        fields = "__all__"

    def create(self, validated_data):
        article_data = validated_data.pop("article")
        tags_data = validated_data.pop("tags", [])
        genre_for_url_data = validated_data.pop("genre_for_url")
        instance = Art.objects.create(**validated_data)
        Article.objects.create(instance_article=instance, **article_data)
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


class ArtSerializerForGet(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = TagSerializer(many=True)
    genre_for_url = GenreForUrlSerializer()

    class Meta:
        model = Art
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        slug = representation.get("slug", "")
        if slug.endswith("-jp"):
            representation["slug"] = slug[:-3]
        return representation


class ArtSerializerForDestroy(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = TagSerializer(many=True)
    genre_for_url = GenreForUrlSerializer()

    class Meta:
        model = Art
        fields = "__all__"


# ====================================================================================================
class PaintingMethodSerializerForCreateUpdate(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    genre_for_url = serializers.PrimaryKeyRelatedField(
        queryset=GenreForUrl.objects.all()
    )

    class Meta:
        model = PaintingMethod
        fields = "__all__"

    def create(self, validated_data):
        article_data = validated_data.pop("article")
        tags_data = validated_data.pop("tags", [])
        genre_for_url_data = validated_data.pop("genre_for_url")
        instance = PaintingMethod.objects.create(**validated_data)
        Article.objects.create(instance_article=instance, **article_data)
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


class PaintingMethodSerializerForGet(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = TagSerializer(many=True)
    genre_for_url = GenreForUrlSerializer()

    class Meta:
        model = PaintingMethod
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        slug = representation.get("slug", "")
        if slug.endswith("-jp"):
            representation["slug"] = slug[:-3]
        return representation


class PaintingMethodSerializerForDestroy(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = TagSerializer(many=True)
    genre_for_url = GenreForUrlSerializer()

    class Meta:
        model = PaintingMethod
        fields = "__all__"


# ====================================================================================================
class PaintingStyleSerializerForCreateUpdate(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    genre_for_url = serializers.PrimaryKeyRelatedField(
        queryset=GenreForUrl.objects.all()
    )

    class Meta:
        model = PaintingStyle
        fields = "__all__"

    def create(self, validated_data):
        article_data = validated_data.pop("article")
        tags_data = validated_data.pop("tags", [])
        genre_for_url_data = validated_data.pop("genre_for_url")
        instance = PaintingStyle.objects.create(**validated_data)
        Article.objects.create(instance_article=instance, **article_data)
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


class PaintingStyleSerializerForGet(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = TagSerializer(many=True)
    genre_for_url = GenreForUrlSerializer()

    class Meta:
        model = PaintingStyle
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        slug = representation.get("slug", "")
        if slug.endswith("-jp"):
            representation["slug"] = slug[:-3]
        return representation


class PaintingStyleSerializerForDestroy(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = TagSerializer(many=True)
    genre_for_url = GenreForUrlSerializer()

    class Meta:
        model = PaintingStyle
        fields = "__all__"


# ====================================================================================================
class ArtsPeriodSerializerForCreateUpdate(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    genre_for_url = serializers.PrimaryKeyRelatedField(
        queryset=GenreForUrl.objects.all()
    )

    class Meta:
        model = ArtsPeriod
        fields = "__all__"

    def create(self, validated_data):
        article_data = validated_data.pop("article")
        tags_data = validated_data.pop("tags", [])
        genre_for_url_data = validated_data.pop("genre_for_url")
        instance = ArtsPeriod.objects.create(**validated_data)
        Article.objects.create(instance_article=instance, **article_data)
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


class ArtsPeriodSerializerForGet(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = TagSerializer(many=True)
    genre_for_url = GenreForUrlSerializer()

    class Meta:
        model = ArtsPeriod
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        slug = representation.get("slug", "")
        if slug.endswith("-jp"):
            representation["slug"] = slug[:-3]
        return representation


class ArtsPeriodSerializerForDestroy(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = TagSerializer(many=True)
    genre_for_url = GenreForUrlSerializer()

    class Meta:
        model = ArtsPeriod
        fields = "__all__"


# ====================================================================================================
class ArtistSerializerForCreateUpdate(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    genre_for_url = serializers.PrimaryKeyRelatedField(
        queryset=GenreForUrl.objects.all()
    )

    class Meta:
        model = Artist
        fields = "__all__"

    def create(self, validated_data):
        article_data = validated_data.pop("article")
        tags_data = validated_data.pop("tags", [])
        genre_for_url_data = validated_data.pop("genre_for_url")
        instance = Artist.objects.create(**validated_data)
        Article.objects.create(instance_article=instance, **article_data)
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


class ArtistSerializerForGet(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = TagSerializer(many=True)
    genre_for_url = GenreForUrlSerializer()

    class Meta:
        model = Artist
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        slug = representation.get("slug", "")
        if slug.endswith("-jp"):
            representation["slug"] = slug[:-3]
        return representation


class ArtistSerializerForDestroy(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = TagSerializer(many=True)
    genre_for_url = GenreForUrlSerializer()

    class Meta:
        model = Artist
        fields = "__all__"


# ====================================================================================================
class MuseumSerializerForCreateUpdate(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    genre_for_url = serializers.PrimaryKeyRelatedField(
        queryset=GenreForUrl.objects.all()
    )

    class Meta:
        model = Museum
        fields = "__all__"

    def create(self, validated_data):
        article_data = validated_data.pop("article")
        tags_data = validated_data.pop("tags", [])
        genre_for_url_data = validated_data.pop("genre_for_url")
        instance = Museum.objects.create(**validated_data)
        Article.objects.create(instance_article=instance, **article_data)
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


class MuseumSerializerForGet(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = TagSerializer(many=True)
    genre_for_url = GenreForUrlSerializer()

    class Meta:
        model = Museum
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        slug = representation.get("slug", "")
        if slug.endswith("-jp"):
            representation["slug"] = slug[:-3]
        return representation


class MuseumSerializerForDestroy(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = TagSerializer(many=True)
    genre_for_url = GenreForUrlSerializer()

    class Meta:
        model = Museum
        fields = "__all__"
