from django.db import models
from django.utils import timezone
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from countries.models import Country
from general.models import Article, Tag, Genre


class Habitat(models.Model):
    name = models.CharField(max_length=200)
    name_jp = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    excerpt = models.TextField(default="")
    excerpt_jp = models.TextField(default="")
    climate = models.CharField(max_length=200)
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    genre = models.ManyToManyField(Genre, related_name="habitat_genres")
    tag = models.ManyToManyField(Tag, related_name="habitat_tags")

    def __str__(self):
        return self.name


class Species(models.Model):
    SPECIES_CHOICES = [
        ("mammal", "Mammal"),
        ("bird", "Bird"),
        ("reptile", "Reptile"),
        ("fish", "Fish"),
        ("plant", "Plant"),
        ("insect", "Insect"),
        ("amphibian", "Amphibian"),
        ("crustacean", "Crustacean"),
        ("dinosaur", "Dinosaur"),
        ("bacteria", "Bacteria"),
        ("fungi", "Fungi"),
        ("protist", "Protist"),
        ("mollusk", "Mollusk"),
    ]

    name = models.CharField(max_length=200, choices=SPECIES_CHOICES)
    name_jp = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    genre = models.ManyToManyField(Genre, related_name="species_genres")
    excerpt = models.TextField(default="")
    excerpt_jp = models.TextField(default="")
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    tag = models.ManyToManyField(Tag, related_name="species_tags")


class LivingThings(models.Model):
    name = models.CharField(max_length=200)
    name_jp = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    country = models.ManyToManyField(Country, related_name="living_things_countries")
    excerpt = models.TextField(default="")
    excerpt_jp = models.TextField(default="")
    habitat = models.ForeignKey(Habitat, on_delete=models.CASCADE)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    genre = models.ManyToManyField(Genre, related_name="living_things_genres")
    tag = models.ManyToManyField(Tag, related_name="living_things_tags")
