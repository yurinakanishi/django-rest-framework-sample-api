from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from general.models import Article, Tag, Genre


class Knowledge(models.Model):
    TYPE_CHOICES = [("knowledge", "Knowledge"), ("blog", "Blog")]
    name = models.CharField(max_length=100)
    name_jp = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    excerpt = models.TextField(max_length=200, default="")
    excerpt_jp = models.TextField(max_length=200, default="")
    article = models.OneToOneField(Article, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name="knowledge_tags")
    genres = models.ManyToManyField(Genre, related_name="knowledge_genres")
    notesite_url = models.URLField(max_length=200, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)
    knowledge_type = models.CharField(
        max_length=100, choices=TYPE_CHOICES, default="knowledge"
    )

    def __str__(self):
        return self.name
