from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from general.models import Article, Tag, GenreForURL, Language
from django.conf import settings

# class TypeChoices(models.TextChoices):
#     KNOWLEDGE = "knowledge", "Knowledge"
#     BLOG = "blog", "Blog"

# class TypeChoicesJP(models.TextChoices):
#     KNOWLEDGE = "knowledge", "知識"
#     BLOG = "blog", "ブログ"


class Knowledge(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True, related_name="knowledge_tags")
    genre_for_url = models.ForeignKey(
        GenreForURL,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="knowledge_genre_for_url",
    )

    TYPE_CHOICES = [
        ("knowledge", "knowledge"),
        ("blog", "blog"),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default="knowledge")
    notesite_url = models.URLField(max_length=200, null=True, blank=True)
    article = models.OneToOneField(
        Article,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="knowledge_article",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.name
