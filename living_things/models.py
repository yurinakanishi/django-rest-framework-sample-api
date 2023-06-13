from django.db import models
from django.utils import timezone
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from locations.models import Location
from general.models import Article, Tag, Genre


class Habitat(models.Model):
    HABITAT_CHOICES = [
        ("desert", "Desert", "砂漠"),
        ("forest", "Forest", "森林"),
        ("sandy_beach", "Sandy Beach", "砂浜"),
        ("deep_sea", "Deep Sea", "深海"),
        ("savanna", "Savanna", "サバンナ"),
        ("sea", "Sea", "海"),
        ("river", "River", "川"),
        ("rocky_shore", "Rocky Shore", "岩場"),
        ("lake", "Lake", "湖"),
        ("polar", "Polar", "極地"),
        ("tropical_rain_forest", "Tropical Rain Forest", "熱帯雨林"),
    ]
    name = [en for _, en, _ in HABITAT_CHOICES]
    name_jp = [jp for _, _, jp in HABITAT_CHOICES]
    slug = models.SlugField(max_length=200, blank=True)
    excerpt = models.TextField(max_length=200, default="")
    excerpt_jp = models.TextField(max_length=200, default="")
    climate = models.CharField(max_length=200)
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    genres = models.ManyToManyField(Genre, related_name="habitat_genres")
    tags = models.ManyToManyField(Tag, related_name="habitat_tags")

    def __str__(self):
        return self.name


class Species(models.Model):
    SPECIES_CHOICES = [
        ("mammal", "Mammal", "哺乳類"),
        ("bird", "Bird", "鳥類"),
        ("reptile", "Reptile", "爬虫類"),
        ("fish", "Fish", "魚類"),
        ("insect", "Insect", "昆虫"),
        ("amphibian", "Amphibian", "両生類"),
        ("crustacean", "Crustacean", "甲殻類"),
        ("mollusk", "Mollusk", "軟体動物"),
    ]
    name = [en for _, en, _ in SPECIES_CHOICES]
    name_jp = [jp for _, _, jp in SPECIES_CHOICES]
    slug = models.SlugField(max_length=200, blank=True)
    excerpt = models.TextField(max_length=200, default="")
    excerpt_jp = models.TextField(max_length=200, default="")
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag, related_name="species_tags")
    genres = models.ManyToManyField(Genre, related_name="species_genres")


class LivingThings(models.Model):
    name = models.CharField(max_length=100)
    name_jp = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    location = models.ManyToManyField(Location, related_name="living_things_countries")
    excerpt = models.TextField(max_length=200, default="")
    excerpt_jp = models.TextField(max_length=200, default="")
    habitat = models.ForeignKey(Habitat, on_delete=models.CASCADE)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    genres = models.ManyToManyField(Genre, related_name="living_things_genres")
    tags = models.ManyToManyField(Tag, related_name="living_things_tags")
