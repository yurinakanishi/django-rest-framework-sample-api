from django.db import models
from django.utils import timezone
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from locations.models import Location
from general.models import Article, Tag, GenreForURL, Language


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
        ("砂漠", "Desert jp"),
        ("森林", "Forest jp"),
        ("砂浜", "Sandy Beach jp"),
        ("深海", "Deep Sea jp"),
        ("サバンナ", "Savanna jp"),
        ("海", "Sea jp"),
        ("川", "River jp"),
        ("岩場", "Rocky Shore jp"),
        ("湖", "Lake jp"),
        ("極地", "Polar jp"),
        ("熱帯雨林", "Tropical Rain Forest jp"),
    ]

    name = models.CharField(max_length=200, choices=HABITAT_CHOICES)
    slug = models.SlugField(max_length=200, unique=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
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
        ("哺乳類", "Mammal jp"),
        ("鳥類", "Bird jp"),
        ("爬虫類", "Reptile jp"),
        ("魚類", "Fish jp"),
        ("昆虫", "Insect jp"),
        ("両生類", "Amphibian jp"),
        ("甲殻類", "Crustacean jp"),
        ("軟体動物", "Mollusk jp"),
    ]

    name = models.CharField(max_length=200, choices=SPECIES_CHOICES)
    slug = models.SlugField(max_length=200, unique=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
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
    slug = models.SlugField(max_length=100, unique=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    location = models.ManyToManyField(
        Location, blank=True, related_name="living_things_countries"
    )
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
