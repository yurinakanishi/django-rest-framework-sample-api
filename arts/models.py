from django.db import models
from general.models import Article, Tag, GenreForURL, Language
from locations.models import Location
from dates.models import Date, Period
from people.models import Person


class Museum(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, blank=True, null=True
    )
    article = models.OneToOneField(
        Article, on_delete=models.CASCADE, blank=True, null=True
    )
    genre_for_url = models.ForeignKey(
        GenreForURL,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="museums_genre_for_url",
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="museums_tags")

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=100)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    article = models.OneToOneField(
        Article, on_delete=models.CASCADE, blank=True, null=True
    )
    genre_for_url = models.ForeignKey(
        GenreForURL,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="artists_genre_for_url",
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="artists_tags")

    def __str__(self):
        return self.name


class PaintingMethod(models.Model):
    METHODS_CHOICES = [
        ("oil-painting", "Oil Painting"),
        ("pastel-painting", "Pastel Painting"),
        ("watercolor-painting", "Watercolor Painting"),
    ]

    name = models.CharField(max_length=200, choices=METHODS_CHOICES)
    slug = models.SlugField(max_length=200, unique=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE, blank=True, null=True)
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, blank=True, null=True
    )
    article = models.OneToOneField(
        Article, on_delete=models.CASCADE, blank=True, null=True
    )
    genre_for_url = models.ForeignKey(
        GenreForURL,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="painting_methods_genre_for_url",
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="painting_methods_tags")

    def __str__(self):
        return self.name


class PaintingStyle(models.Model):
    STYLES_CHOICES = [
        ("modernism", "Modernism"),
        ("impressionism", "Impressionism"),
        ("abstract-styles", "Abstract styles"),
        ("realism", "Realism"),
        ("photorealism", "Photorealism"),
        ("surrealism", "Surrealism"),
        ("expressionism", "Expressionism"),
        ("cubism", "Cubism"),
        ("chinese-style", "Chinese Style"),
        ("japanese-style", "Japanese Style"),
        ("indian-style", "Indian Style"),
    ]

    name = models.CharField(max_length=200, choices=STYLES_CHOICES)
    slug = models.SlugField(max_length=100, unique=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE, blank=True, null=True)
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, blank=True, null=True
    )
    article = models.OneToOneField(
        Article, on_delete=models.CASCADE, blank=True, null=True
    )
    genre_for_url = models.ForeignKey(
        GenreForURL,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="painting_styles_genre_for_url",
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="painting_styles_tags")

    def __str__(self):
        return self.name


class Art(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, null=True)
    year_made = models.ForeignKey(Date, on_delete=models.CASCADE, blank=True, null=True)
    museum = models.ForeignKey(Museum, on_delete=models.SET_NULL, null=True, blank=True)
    estimate_value = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    article = models.OneToOneField(
        Article, on_delete=models.CASCADE, blank=True, null=True
    )
    genre_for_url = models.ForeignKey(
        GenreForURL,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="arts_genre_for_url",
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="arts_tags")
    method = models.ForeignKey(
        PaintingMethod,
        on_delete=models.SET_NULL,
        related_name="arts_methods",
        blank=True,
        null=True,
    )
    style = models.ForeignKey(
        PaintingStyle,
        on_delete=models.SET_NULL,
        related_name="arts_styles",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
