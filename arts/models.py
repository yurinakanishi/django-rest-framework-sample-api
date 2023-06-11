from django.db import models
from general.models import Article, Tag, Genre


class Museum(models.Model):
    name = models.CharField(max_length=200)
    name_jp = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    location = models.CharField(max_length=200)
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    genre = models.ManyToManyField(Genre, related_name="museums_genres")
    tag = models.ManyToManyField(Tag, related_name="museums_tags")

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=100)
    name_jp = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    genre = models.ManyToManyField(Genre, related_name="artists_genres")
    tag = models.ManyToManyField(Tag, related_name="artists_tags")

    def __str__(self):
        return self.name


class Art(models.Model):
    title = models.CharField(max_length=200)
    title_jp = models.CharField(max_length=100)
    excerpt = models.TextField(default="")
    excerpt_jp = models.TextField(default="")
    slug = models.SlugField(max_length=200, unique=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    year_made = models.IntegerField()
    museum = models.ForeignKey(Museum, on_delete=models.SET_NULL, null=True, blank=True)
    estimate_value = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    genre = models.ManyToManyField(Genre, related_name="arts_genres")
    tag = models.ManyToManyField(Tag, related_name="arts_tags")

    def __str__(self):
        return self.title


class PaintingMethod(models.Model):
    name = models.CharField(max_length=200)
    name_jp = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    excerpt = models.TextField(default="")
    excerpt_jp = models.TextField(default="")
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    genre = models.ManyToManyField(Genre, related_name="painting_methods_genres")
    tag = models.ManyToManyField(Tag, related_name="painting_methods_tags")

    def __str__(self):
        return self.name


class PaintingStyle(models.Model):
    name = models.CharField(max_length=200)
    name_jp = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    excerpt = models.TextField(default="")
    excerpt_jp = models.TextField(default="")
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    genre = models.ManyToManyField(Genre, related_name="painting_styles_genres")
    tag = models.ManyToManyField(Tag, related_name="painting_styles_tags")

    def __str__(self):
        return self.name
