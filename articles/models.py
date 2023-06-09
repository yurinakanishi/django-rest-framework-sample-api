from django.db import models
from django.utils import timezone
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


class MovieDirector(models.Model):
    name = models.CharField(max_length=100, unique=True)
    name_ja = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    name_ja = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    name_ja = models.CharField(max_length=100, unique=True)
    hierarchy = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class MovieRating(models.Model):
    story = models.FloatField(default=0.0)
    socialEffect = models.FloatField(default=0.0)
    businessSuccessful = models.FloatField(default=0.0)
    images = models.FloatField(default=0.0)
    innovative = models.FloatField(default=0.0)
    music = models.FloatField(default=0.0)
    rating_average = models.FloatField(default=0.0)


class Movie(models.Model):
    title = models.CharField(max_length=200)
    title_jp = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    release_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="movies")
    director = models.ForeignKey(
        MovieDirector, on_delete=models.CASCADE, related_name="movies"
    )
    runtime = models.IntegerField(help_text="Duration in minutes")
    movie_rating = models.ForeignKey(MovieRating, on_delete=models.CASCADE, null=True)
    poster = models.ImageField(upload_to="posters/", null=True, blank=True)
    back_drop = models.ImageField(upload_to="back_drops/", null=True, blank=True)
    over_view = models.TextField(default="")
    media_type = models.CharField(max_length=100, default="movie")
    themoviedb_id = models.CharField(max_length=100, default="")


class Article(models.Model):
    title = models.CharField(max_length=200)
    title_jp = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = RichTextUploadingField(blank=True, null=True)
    content_jp = RichTextUploadingField(blank=True, null=True)
    references = models.TextField(default="")
    references_jp = models.TextField(default="")
    excerpt = models.TextField(default="")
    excerpt_jp = models.TextField(default="")
    notesite_url = models.CharField(max_length=100, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    rating = models.FloatField(default=0.0)
    rating_count = models.IntegerField(default=0)
    movie_info = models.ForeignKey(
        Movie, on_delete=models.CASCADE, null=True, blank=True, default=None
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f" {self.pk} {self.title}"

    class Meta:
        ordering = ["-published_date"]
