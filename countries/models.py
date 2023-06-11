from django.db import models
from general.models import Article, Tag, Genre


class Country(models.Model):
    name = models.CharField(max_length=100)
    name_jp = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    excerpt = models.TextField(default="")
    excerpt_jp = models.TextField(default="")
    capital_city = models.CharField(max_length=100)
    population = models.IntegerField()
    area = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=50)
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    genre = models.ManyToManyField(Genre, related_name="movies")
    tag = models.ManyToManyField(Tag, related_name="movies")

    def __str__(self):
        return self.name
