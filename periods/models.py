from django.db import models
from django.db import models
from django.utils import timezone
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from general.models import Article, Tag, Genre


class Period(models.Model):
    name = models.CharField(max_length=100, unique=True)
    name_ja = models.CharField(max_length=100, unique=True)
    excerpt = models.TextField(default="")
    excerpt_jp = models.TextField(default="")
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    genre = models.ManyToManyField(Genre, related_name="period_genres")
    tag = models.ManyToManyField(Tag, related_name="period_tags")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
