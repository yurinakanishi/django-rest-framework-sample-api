from django.db import models
from django.utils import timezone
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, default="")
    name_ja = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, default="")
    name_ja = models.CharField(max_length=100, unique=True)
    hierarchy = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("hierarchy",)


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, default="")
    content = RichTextUploadingField(blank=True)
    content_jp = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    references_jp = RichTextUploadingField(blank=True)
    rating = models.FloatField(default=0.0)
    rating_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-pk"]
