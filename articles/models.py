from django.db import models
from django.utils import timezone
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    name_ja = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    name_ja = models.CharField(max_length=100, unique=True)
    hierarchy = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Article(models.Model):
    title = models.CharField(max_length=200)
    title_jp = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = RichTextUploadingField(blank=True, null=True)
    content_jp = RichTextUploadingField(blank=True, null=True)
    excerpt = models.TextField(default="")
    excerpt_jp = models.TextField(default="")
    notesite_url = models.CharField(max_length=100, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f" {self.pk} {self.title}"

    class Meta:
        ordering = ["-published_date"]
