from django.db import models
from django.utils import timezone
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from general.models import Article, Tag, GenreForUrl, Language
from people.models import Person


class MovieDirector(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, blank=True)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    article = models.OneToOneField(
        Article, on_delete=models.SET_NULL, blank=True, null=True
    )
    genre = models.ForeignKey(
        GenreForUrl,
        null=True,
        on_delete=models.CASCADE,
        related_name="movie_director_genre_for_url",
        blank=True,
    )
    tag = models.ManyToManyField(Tag, blank=True, related_name="movie_director_tags")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class MovieActor(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True)
    article = models.OneToOneField(
        Article, on_delete=models.SET_NULL, null=True, blank=True
    )
    genre = models.ForeignKey(
        GenreForUrl,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="movie_actor_genre_for_url",
    )
    tag = models.ManyToManyField(Tag, blank=True, related_name="movie_actor_tags")

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1
    )


class MovieRating(models.Model):
    RATING_CHOICES = (
        (0, "0"),
        (0.5, "0.5"),
        (1, "1"),
        (1.5, "1.5"),
        (2, "2"),
        (2.5, "2.5"),
        (3, "3"),
        (3.5, "3.5"),
        (4, "4"),
        (4.5, "4.5"),
        (5, "5"),
    )
    story = models.PositiveSmallIntegerField(blank=True, choices=RATING_CHOICES)
    social_effect = models.PositiveSmallIntegerField(blank=True, choices=RATING_CHOICES)
    business_successful = models.PositiveSmallIntegerField(
        blank=True, choices=RATING_CHOICES
    )
    images = models.PositiveSmallIntegerField(blank=True, choices=RATING_CHOICES)
    innovative = models.PositiveSmallIntegerField(blank=True, choices=RATING_CHOICES)
    music = models.PositiveSmallIntegerField(blank=True, choices=RATING_CHOICES)
    rating_average = models.PositiveSmallIntegerField(
        blank=True, choices=RATING_CHOICES
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1
    )


class Movie(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    TYPE_CHOICES = (
        ("movie", "movie"),
        ("tv", "tv"),
    )
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    release_date = models.DateField(null=True, blank=True)
    director = models.ForeignKey(
        MovieDirector,
        on_delete=models.SET_NULL,
        related_name="directed_movies",
        blank=True,
        null=True,
    )
    actors = models.ManyToManyField(Person, blank=True, related_name="movie_actors")
    runtime = models.IntegerField(
        help_text="Duration in minutes", blank=True, null=True
    )
    poster = models.ImageField(upload_to="posters/", null=True, blank=True)
    back_drop = models.ImageField(upload_to="back_drops/", null=True, blank=True)
    over_view = models.TextField(blank=True)
    themoviedb_id = models.CharField(max_length=100, blank=True)
    article = models.OneToOneField(
        Article, on_delete=models.SET_NULL, null=True, blank=True
    )
    article = models.OneToOneField(
        Article,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="movie_article",
    )

    movie_rating = models.OneToOneField(
        MovieRating,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="movie_ratings",
    )
    genre_for_url = models.ForeignKey(
        GenreForUrl,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="movie_genre_for_url",
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="movie_tags")

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1
    )

    def __str__(self):
        return self.name
