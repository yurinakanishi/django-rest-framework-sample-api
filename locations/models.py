from django.db import models
from general.models import Article, Tag, GenreForURL


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    name_jp = models.CharField(max_length=100, unique=True, blank=True)
    slug = models.SlugField(max_length=100, blank=True)
    excerpt = models.TextField(max_length=200, blank=True)
    excerpt_jp = models.TextField(max_length=200, blank=True)
    capital_city = models.CharField(max_length=100, blank=True)
    population = models.IntegerField(blank=True, null=True)
    area_km2 = models.IntegerField(blank=True, null=True)
    currency = models.CharField(max_length=50, blank=True)
    article = models.OneToOneField(
        Article, on_delete=models.CASCADE, blank=True, null=True
    )
    genre_for_url = models.ForeignKey(
        GenreForURL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="countries",
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="countries")

    def __str__(self):
        return self.name


class Location(models.Model):
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, blank=True, null=True
    )
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    street_address = models.CharField(max_length=100, blank=True)
