from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from general.models import Article, Tag, Genre


class Knowledge(models.Model):
    TYPE_CHOICES = [
        ("knowledge", "Knowledge"),
        ("blog", "Blog"),
    ]

    TYPE_CHOICES_JP = [
        ("knowledge", "知識"),
        ("blog", "ブログ"),
    ]

    type_en = models.CharField(max_length=20, choices=TYPE_CHOICES, default="knowledge")
    type_jp = models.CharField(
        max_length=20, choices=TYPE_CHOICES_JP, default="knowledge"
    )
    name = models.CharField(max_length=100)
    name_jp = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    excerpt = models.TextField(max_length=200, blank=True)
    excerpt_jp = models.TextField(max_length=200, blank=True)
    article = models.OneToOneField(
        Article,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="knowledge_articles",
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="knowledge_tags")
    genres = models.ManyToManyField(Genre, blank=True, related_name="knowledge_genres")
    kicker = models.CharField(max_length=100, blank=True)
    notesite_url = models.URLField(max_length=200, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    published_date = models.DateTimeField(default=timezone.now, blank=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True)
    knowledge_type = models.CharField(
        max_length=100, choices=TYPE_CHOICES, default="knowledge", blank=True
    )

    def __str__(self):
        return self.name
