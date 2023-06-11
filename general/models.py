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
    content = RichTextUploadingField(blank=True, null=True)
    content_jp = RichTextUploadingField(blank=True, null=True)
    references = RichTextUploadingField(blank=True, null=True)
    references_jp = RichTextUploadingField(blank=True, null=True)
    rating = models.FloatField(default=0.0)
    rating_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Article ID: {self.pk}"

    class Meta:
        ordering = [
            "-pk"
        ]  # if you want to order by creation, you can use the primary key.
