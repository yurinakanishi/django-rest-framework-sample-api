from django.db import models
from django.utils import timezone
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from general.models import Article, Tag, Genre
from locations.models import Location


class Person(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    name_jp = models.CharField(max_length=100, unique=True)
    excerpt = models.TextField(max_length=200, default="")
    excerpt_jp = models.TextField(max_length=200, default="")
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)
    born_in = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True, blank=True
    )
    article = models.OneToOneField(
        Article, on_delete=models.SET_NULL, null=True, blank=True
    )
    genres = models.ManyToManyField(Genre, related_name="person_genres")
    tags = models.ManyToManyField(Tag, related_name="person_tags")
    occupation = models.CharField(max_length=100, default="")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
