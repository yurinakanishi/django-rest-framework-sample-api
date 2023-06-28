from django.db import models
from django.utils import timezone
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from general.models import Article, Tag, GenreForURL, Language
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
        GenreForURL,
        null=True,
        on_delete=models.CASCADE,
        related_name="movie_director_genre_for_url",
        blank=True,
    )
    tag = models.ManyToManyField(Tag, blank=True, related_name="movie_director_tags")

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
        GenreForURL,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="movie_actor_genre_for_url",
    )
    tag = models.ManyToManyField(Tag, blank=True, related_name="movie_actor_tags")


class Movie(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
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
    media_type = models.CharField(max_length=100, default="movie", blank=True)
    themoviedb_id = models.CharField(max_length=100, blank=True)
    article = models.OneToOneField(
        Article, on_delete=models.SET_NULL, null=True, blank=True
    )
    genre_for_url = models.ForeignKey(
        GenreForURL,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="movie_genre_for_url",
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="movie_tags")

    def __str__(self):
        return self.name


class MovieRating(models.Model):
    movie_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="movie_rating_user",
    )
    RATING_CHOICES = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
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


class MovieReview(models.Model):
    name = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    article = models.OneToOneField(
        Article,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="movie_review_articles",
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="movie_review_movie",
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="movie_review_tags")
    genre_for_url = models.ForeignKey(
        GenreForURL,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="movie_review_genre_for_url",
    )
    kicker = models.CharField(max_length=100, blank=True)
    rating = models.OneToOneField(
        MovieRating,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="movie_ratings",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )
    published_date = models.DateTimeField(default=timezone.now, blank=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f"Review for {self.movie} by {self.user}"
