from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from general.models import Article, Tag, Genre


class Knowledge(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    excerpt = models.TextField(default="")
    excerpt_jp = models.TextField(default="")
    article = models.OneToOneField(Article, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, related_name="knowledge_tags")
    genre = models.ManyToManyField(Genre, related_name="knowledge_genres")
    notesite_url = models.CharField(max_length=100, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=100, default="knowledge")

    def __str__(self):
        return self.name
