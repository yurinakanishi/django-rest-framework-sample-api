from django.db import models
from django.utils import timezone
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from general.models import Article, Tag, Genre
from people.models import Person


class MovieDirector(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, blank=True)
    name_jp = models.CharField(max_length=100, unique=True)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    excerpt = models.TextField(max_length=200, default="")
    excerpt_jp = models.TextField(max_length=200, default="")
    article = models.OneToOneField(Article, on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre, related_name="movie_director_genres")
    tag = models.ManyToManyField(Tag, related_name="movie_director_tags")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class MovieActor(models.Model):
    name = models.CharField(max_length=100, unique=True)
    name_jp = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, blank=True)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True)
    excerpt = models.TextField(max_length=200, default="")
    excerpt_jp = models.TextField(max_length=200, default="")
    article = models.OneToOneField(
        Article, on_delete=models.SET_NULL, null=True, blank=True
    )
    genre = models.ManyToManyField(Genre, related_name="movie_actor_genres", blank=True)
    tag = models.ManyToManyField(Tag, related_name="movie_actor_tags", blank=True)


class MovieRating(models.Model):
    story = models.FloatField(default=0.0)
    social_effect = models.FloatField(default=0.0)
    business_successful = models.FloatField(default=0.0)
    images = models.FloatField(default=0.0)
    innovative = models.FloatField(default=0.0)
    music = models.FloatField(default=0.0)
    rating_average = models.FloatField(default=0.0)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    title_jp = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    excerpt = models.TextField(max_length=200, default="")
    excerpt_jp = models.TextField(max_length=200, default="")
    release_date = models.DateField()
    director = models.ForeignKey(
        MovieDirector,
        on_delete=models.SET_NULL,
        related_name="directed_movies",
        null=True,
    )
    actors = models.ManyToManyField(Person, related_name="acted_in_movies")
    runtime = models.IntegerField(help_text="Duration in minutes")
    movie_rating = models.ForeignKey(
        MovieRating, on_delete=models.SET_NULL, null=True, related_name="movie_ratings"
    )
    poster = models.ImageField(upload_to="posters/", null=True, blank=True)
    back_drop = models.ImageField(upload_to="back_drops/", null=True, blank=True)
    over_view = models.TextField(default="")
    media_type = models.CharField(max_length=100, default="movie")
    themoviedb_id = models.CharField(max_length=100, default="")
    article = models.OneToOneField(
        Article, on_delete=models.SET_NULL, null=True, blank=True
    )
    genres = models.ManyToManyField(Genre, related_name="movie_genres")
    tags = models.ManyToManyField(Tag, related_name="movie_tags")


class MovieReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    review_text = RichTextUploadingField()
    rating = models.ForeignKey(MovieRating, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ["user", "movie"]

    def __str__(self):
        return f"Review for {self.movie.title} by {self.user.username}"
