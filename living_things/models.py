from django.db import models
from django.utils import timezone
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from locations.models import Location
from general.models import Article, Tag, GenreForURL


class Habitat(models.Model):
    HABITAT_CHOICES = [
        ("desert", "Desert"),
        ("forest", "Forest"),
        ("sandy-beach", "Sandy Beach"),
        ("deep-sea", "Deep Sea"),
        ("savanna", "Savanna"),
        ("sea", "Sea"),
        ("river", "River"),
        ("rocky-shore", "Rocky Shore"),
        ("lake", "Lake"),
        ("polar", "Polar"),
        ("tropical-rain-forest", "Tropical Rain Forest"),
    ]

    HABITAT_CHOICES_JP = [
        ("desert", "砂漠"),
        ("forest", "森林"),
        ("sandy-beach", "砂浜"),
        ("deep-sea", "深海"),
        ("savanna", "サバンナ"),
        ("sea", "海"),
        ("river", "川"),
        ("rocky-shore", "岩場"),
        ("lake", "湖"),
        ("polar", "極地"),
        ("tropical-rain-forest", "熱帯雨林"),
    ]

    name = models.CharField(max_length=200, choices=HABITAT_CHOICES)
    name_jp = models.CharField(max_length=200, choices=HABITAT_CHOICES_JP, blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    excerpt = models.TextField(max_length=200, blank=True)
    excerpt_jp = models.TextField(max_length=200, blank=True)
    climate = models.CharField(max_length=200, blank=True)
    article = models.OneToOneField(
        Article, on_delete=models.CASCADE, blank=True, null=True
    )
    genre_for_url = models.ForeignKey(
        GenreForURL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="habitat_genre_for_url",
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="habitat_tags")

    def __str__(self):
        return self.name


class Species(models.Model):
    SPECIES_CHOICES = [
        ("mammal", "Mammal"),
        ("bird", "Bird"),
        ("reptile", "Reptile"),
        ("fish", "Fish"),
        ("insect", "Insect"),
        ("amphibian", "Amphibian"),
        ("crustacean", "Crustacean"),
        ("mollusk", "Mollusk"),
    ]

    SPECIES_CHOICES_JP = [
        ("mammal", "哺乳類"),
        ("bird", "鳥類"),
        ("reptile", "爬虫類"),
        ("fish", "魚類"),
        ("insect", "昆虫"),
        ("amphibian", "両生類"),
        ("crustacean", "甲殻類"),
        ("mollusk", "軟体動物"),
    ]

    name = models.CharField(max_length=200, choices=SPECIES_CHOICES)
    name_jp = models.CharField(max_length=200, choices=SPECIES_CHOICES_JP, blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    excerpt = models.TextField(max_length=200, blank=True)
    excerpt_jp = models.TextField(max_length=200, blank=True)
    article = models.OneToOneField(
        Article, on_delete=models.CASCADE, blank=True, null=True
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="species_tags")
    genre_for_url = models.ForeignKey(
        GenreForURL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="species_genre_for_url",
    )

    def __str__(self):
        return self.name


class LivingThings(models.Model):
    name = models.CharField(max_length=100)
    name_jp = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    location = models.ManyToManyField(
        Location, blank=True, related_name="living_things_countries"
    )
    excerpt = models.TextField(max_length=200, blank=True)
    excerpt_jp = models.TextField(max_length=200, blank=True)
    habitat = models.ForeignKey(
        Habitat, on_delete=models.CASCADE, blank=True, null=True
    )
    species = models.ForeignKey(
        Species, on_delete=models.CASCADE, blank=True, null=True
    )
    article = models.OneToOneField(
        Article, on_delete=models.CASCADE, blank=True, null=True
    )
    genre_for_url = models.ForeignKey(
        GenreForURL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="living_things_genre_for_url",
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="living_things_tags")

    def __str__(self):
        return self.name
