from django.db import models
from django.utils import timezone
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from general.models import Article, Tag, GenreForUrl, Language
from locations.models import Location


class Person(models.Model):
    name = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    born_in = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True, blank=True
    )
    article = models.OneToOneField(
        Article, on_delete=models.SET_NULL, null=True, blank=True
    )
    genre_for_url = models.ForeignKey(
        GenreForUrl,
        null=True,
        on_delete=models.CASCADE,
        blank=True,
        related_name="person_genre_for_url",
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="person_tags")
    occupation = models.CharField(max_length=100, blank=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
