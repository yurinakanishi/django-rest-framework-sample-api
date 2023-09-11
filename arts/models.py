from django.db import models
from general.models import Article, Tag, GenreForUrl, Language
from locations.models import Location
from dates.models import Date, Period
from people.models import Person
from django.conf import settings


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
        GenreForUrl,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="museums_genre_for_url",
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="museums_tags")

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1
    )

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
        GenreForUrl,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="artists_genre_for_url",
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="artists_tags")

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1
    )

    def __str__(self):
        return self.name


class PaintingMethod(models.Model):
    METHODS_CHOICES = [
        ("oil-painting", "Oil Painting"),
        ("pastel-painting", "Pastel Painting"),
        ("watercolor-painting", "Watercolor Painting"),
        ("油絵", "Oil Painting jp"),
        ("パステル画", "Pastel Painting jp"),
        ("水彩画", "Watercolor Painting jp"),
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
        GenreForUrl,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="painting_methods_genre_for_url",
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="painting_methods_tags")

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1
    )

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
        ("モダニズム", "Modernism jp"),
        ("印象派", "Impressionism jp"),
        ("抽象派", "Abstract styles jp"),
        ("写実主義", "Realism jp"),
        ("フォトリアリズム", "Photorealism jp"),
        ("シュールレアリスム", "Surrealism jp"),
        ("表現主義", "Expressionism jp"),
        ("キュビズム", "Cubism jp"),
        ("中国画", "Chinese Style jp"),
        ("日本画", "Japanese Style jp"),
        ("インド画", "Indian Style jp"),
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
        GenreForUrl,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="painting_styles_genre_for_url",
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="painting_styles_tags")

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1
    )

    def __str__(self):
        return self.name


class ArtsPeriod(models.Model):
    PERIOD_CHOICES = [
        ("ancient_times", "Ancient Times"),
        ("500s_1300s", "500s-1300s"),
        ("1400s", "1400s"),
        ("1500s", "1500s"),
        ("1600s", "1600s"),
        ("1700s", "1700s"),
        ("1800s", "1800s"),
        ("1900s", "1900s"),
        ("2000s", "2000s"),
        ("古代", "Ancient Times jp"),
        ("500年代-1300年代", "500s-1300s jp"),
        ("1400年代", "1400s jp"),
        ("1500年代", "1500s jp"),
        ("1600年代", "1600s jp"),
        ("1700年代", "1700s jp"),
        ("1800年代", "1800s jp"),
        ("1900年代", "1900s jp"),
        ("2000年代", "2000s jp"),
    ]

    name = models.CharField(max_length=200, choices=PERIOD_CHOICES)
    slug = models.SlugField(max_length=100, unique=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE, blank=True, null=True)
    article = models.OneToOneField(
        Article, on_delete=models.CASCADE, blank=True, null=True
    )
    genre_for_url = models.ForeignKey(
        GenreForUrl,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="arts_period_genre_for_url",
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="arts_period_tags")

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1
    )

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
        GenreForUrl,
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

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1
    )

    def __str__(self):
        return self.name
