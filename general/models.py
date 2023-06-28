from django.db import models
from django.utils import timezone
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class GenreForURL(models.Model):
    NAME_CHOICES = [
        ("knowledge", "knowledge"),
        ("arts/each", "arts/each"),
        ("arts/periods", "arts/periods"),
        ("arts/painting-styles", "arts/painting-styles"),
        ("arts/painting-methods", "arts/painting-methods"),
        ("living-things_each", "living-things_each"),
        ("living-things-habitats", "living-things-habitats"),
        ("living-things-specie", "living-things-species"),
        ("foods/cooking-methods", "foods/cooking-methods"),
        ("foods/ingredients", "foods/ingredients"),
        ("movies", "movies"),
    ]
    name = models.CharField(max_length=100, unique=True, choices=NAME_CHOICES)

    def __str__(self):
        return self.name


class Article(models.Model):
    excerpt = models.TextField(max_length=200, blank=True)
    kicker = models.CharField(max_length=100, blank=True)
    content = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    rating = models.FloatField(default=0.0)
    rating_count = models.IntegerField(blank=True, null=True)
    published_date = models.DateTimeField(default=timezone.now, blank=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.excerpt

    class Meta:
        ordering = ["-pk"]


class Language(models.Model):
    NAME_CHOICES = [
        ("en", "english"),
        ("jp", "japanese"),
    ]
    name = models.CharField(max_length=100, unique=True, choices=NAME_CHOICES)
