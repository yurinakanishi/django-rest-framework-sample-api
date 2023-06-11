from django.db import models
from django.utils import timezone
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from general.models import Article, Tag, Genre


class MovieDirector(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    name_jp = models.CharField(max_length=100, unique=True)
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    genre = models.ManyToManyField(Genre, related_name="movie_director_genres")
    tag = models.ManyToManyField(Tag, related_name="movie_director_tags")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class MovieRating(models.Model):
    story = models.FloatField(default=0.0)
    social_effect = models.FloatField(default=0.0)
    business_successful = models.FloatField(default=0.0)
    images = models.FloatField(default=0.0)
    innovative = models.FloatField(default=0.0)
    music = models.FloatField(default=0.0)
    rating_average = models.FloatField(default=0.0)


class MovieActor(models.Model):
    name = models.CharField(max_length=100, unique=True)
    name_jp = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    genre = models.ManyToManyField(Genre, related_name="movie_actor_genres")
    tag = models.ManyToManyField(Tag, related_name="movie_actor_tags")


class Movie(models.Model):
    title = models.CharField(max_length=200)
    title_jp = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    release_date = models.DateField()
    director = models.ForeignKey(
        MovieDirector, on_delete=models.CASCADE, null=True
    )  # Add this line
    runtime = models.IntegerField(help_text="Duration in minutes")
    movie_rating = models.ForeignKey(
        MovieRating, on_delete=models.CASCADE, null=True, related_name="movie_ratings"
    )
    poster = models.ImageField(upload_to="posters/", null=True, blank=True)
    back_drop = models.ImageField(upload_to="back_drops/", null=True, blank=True)
    over_view = models.TextField(default="")
    media_type = models.CharField(max_length=100, default="movie")
    themoviedb_id = models.CharField(max_length=100, default="")
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    genre = models.ManyToManyField(Genre, related_name="movie_genres")
    tag = models.ManyToManyField(Tag, related_name="movie_tags")
