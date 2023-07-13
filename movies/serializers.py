from rest_framework import serializers
from .models import Movie, MovieActor, MovieRating, MovieDirector
from general.serializers import TagSerializer, GenreForUrlSerializer, ArticleSerializer
from general.models import Tag, GenreForUrl, Article


class MovieRatingSerializerForCreateUpdate(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    genre_for_url = serializers.PrimaryKeyRelatedField(
        many=True, queryset=GenreForUrl.objects.all()
    )

    class Meta:
        model = MovieRating
        fields = "__all__"

    def create(self, validated_data):
        article_data = validated_data.pop("article")
        tags_data = validated_data.pop("tags", [])
        genre_for_url_data = validated_data.pop("genre_for_url")
        instance = MovieRating.objects.create(**validated_data)
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


class MovieRatingSerializerForGet(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = TagSerializer(many=True)
    genre_for_url = GenreForUrlSerializer()

    class Meta:
        model = MovieRating
        fields = "__all__"


class MovieRatingSerializerForDestroy(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = TagSerializer(many=True)
    genre_for_url = GenreForUrlSerializer()

    class Meta:
        model = MovieRating
        fields = "__all__"


class MovieSerializerForCreateUpdate(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    genre_for_url = serializers.PrimaryKeyRelatedField(
        many=True, queryset=GenreForUrl.objects.all()
    )

    class Meta:
        model = Movie
        fields = "__all__"

    def create(self, validated_data):
        article_data = validated_data.pop("article")
        tags_data = validated_data.pop("tags", [])
        genre_for_url_data = validated_data.pop("genre_for_url")
        instance = Movie.objects.create(**validated_data)
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


class MovieSerializerForGet(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = TagSerializer(many=True)
    genre_for_url = GenreForUrlSerializer()

    class Meta:
        model = Movie
        fields = "__all__"


class MovieSerializerForDestroy(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = TagSerializer(many=True)
    genre_for_url = GenreForUrlSerializer()

    class Meta:
        model = Movie
        fields = "__all__"


class MovieActorSerializerForCreateUpdate(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    genre_for_url = serializers.PrimaryKeyRelatedField(
        many=True, queryset=GenreForUrl.objects.all()
    )

    class Meta:
        model = MovieActor
        fields = "__all__"

    def create(self, validated_data):
        article_data = validated_data.pop("article")
        tags_data = validated_data.pop("tags", [])
        genre_for_url_data = validated_data.pop("genre_for_url")
        instance = MovieActor.objects.create(**validated_data)
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


class MovieActorSerializerForGet(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = TagSerializer(many=True)
    genre_for_url = GenreForUrlSerializer()

    class Meta:
        model = MovieActor
        fields = "__all__"


class MovieActorSerializerForDestroy(serializers.ModelSerializer):
    article = ArticleSerializer()
    tags = TagSerializer(many=True)
    genre_for_url = GenreForUrlSerializer()

    class Meta:
        model = MovieActor
        fields = "__all__"
