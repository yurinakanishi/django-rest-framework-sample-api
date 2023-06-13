from django.db import models
from general.models import Article, Tag, Genre
from locations.models import Location
from dates.models import Date, Period
from people.models import Person


class Museum(models.Model):
    name = models.CharField(max_length=100)
    name_jp = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    excerpt = models.TextField(max_length=200, default="")
    excerpt_jp = models.TextField(max_length=200, default="")
    genres = models.ManyToManyField(Genre, related_name="museums_genres")
    tags = models.ManyToManyField(Tag, related_name="museums_tags")

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=100)
    name_jp = models.CharField(max_length=100)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=100, unique=True)
    excerpt = models.TextField(max_length=200, default="")
    excerpt_jp = models.TextField(max_length=200, default="")
    # birth_date = models.DateField()
    # death_date = models.DateField(null=True, blank=True)
    # born_in = models.ForeignKey(
    #     Location, on_delete=models.CASCADE, null=True, blank=True
    # )
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    genres = models.ManyToManyField(Genre, related_name="artists_genres")
    tags = models.ManyToManyField(Tag, related_name="artists_tags")

    def __str__(self):
        return self.name


class ArtMethod(models.Model):
    METHODS_CHOICES = [
        ("oil_painting", "Oil Painting", "油絵"),
        ("pastel_painting", "Pastel Painting", "パステル画"),
        ("watercolor_painting", "Watercolor Painting", "水彩画"),
    ]
    name_en = [en for _, en, _ in METHODS_CHOICES]
    name_jp = [jp for _, _, jp in METHODS_CHOICES]
    slug = models.SlugField(max_length=200, blank=True, unique=True)
    excerpt = models.TextField(max_length=200, default="")
    excerpt_jp = models.TextField(max_length=200, default="")
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    genres = models.ManyToManyField(Genre, related_name="painting_methods_genres")
    tags = models.ManyToManyField(Tag, related_name="painting_methods_tags")

    def __str__(self):
        return self.name


class ArtStyle(models.Model):
    STYLES_CHOICES = [
        ("modernism", "Modernism", "モダニズム"),
        ("impressionism", "Impressionism", "印象派"),
        ("abstract_styles", "Abstract styles", "抽象派"),
        ("realism", "Realism", "リアリズム"),
        ("photorealism", "Photorealism", "フォトリアリズム"),
        ("surrealism", "Surrealism", "シュルレアリズム"),
        ("expressionism", "Expressionism", "表現主義"),
        ("cubism", "Cubism", "キュビズム"),
        ("chinese_style", "Chinese Style", "中国スタイル"),
        ("japanese_style", "Japanese Style", "日本スタイル"),
        ("indian_style", "Indian Style", "インドスタイル"),
    ]
    name = [en for _, en, _ in STYLES_CHOICES]
    name_jp = [jp for _, _, jp in STYLES_CHOICES]
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    excerpt = models.TextField(max_length=200, default="")
    excerpt_jp = models.TextField(max_length=200, default="")
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    genres = models.ManyToManyField(Genre, related_name="painting_styles_genres")
    tags = models.ManyToManyField(Tag, related_name="painting_styles_tags")

    def __str__(self):
        return self.name


class Art(models.Model):
    title = models.CharField(max_length=100)
    title_jp = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    excerpt = models.TextField(max_length=200, default="")
    excerpt_jp = models.TextField(max_length=200, default="")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    year_made = models.ForeignKey(Date, on_delete=models.CASCADE)
    museum = models.ForeignKey(Museum, on_delete=models.SET_NULL, null=True, blank=True)
    estimate_value = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    genres = models.ManyToManyField(Genre, related_name="arts_genres")
    tags = models.ManyToManyField(Tag, related_name="arts_tags")
    method = models.ForeignKey(
        ArtMethod, on_delete=models.SET_NULL, related_name="arts_methods", null=True
    )
    style = models.ForeignKey(
        ArtStyle, on_delete=models.SET_NULL, related_name="arts_styles", null=True
    )

    def __str__(self):
        return self.title
