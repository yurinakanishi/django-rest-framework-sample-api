from django.db import models
from general.models import Article, Tag, Genre


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    name_jp = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, blank=True)
    excerpt = models.TextField(max_length=200, default="")
    excerpt_jp = models.TextField(max_length=200, default="")
    capital_city = models.CharField(max_length=100)
    population = models.IntegerField()
    area = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=50)
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    genres = models.ManyToManyField(Genre, related_name="countries")
    tags = models.ManyToManyField(Tag, related_name="countries")

    def __str__(self):
        return self.name


class Location(models.Model):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    street_address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.state}, {self.country.name}"
