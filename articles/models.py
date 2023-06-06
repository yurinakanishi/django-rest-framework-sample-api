from django.db import models
from django.utils import timezone
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    hierarchy = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Article(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True, null=True)
    LANGUAGE_CHOICES = [(code, name.title()) for code, name in settings.LANGUAGES]
    language = models.CharField(max_length=7, choices=LANGUAGE_CHOICES, default="en")
    excerpt = models.TextField(blank=True)
    notesite_url = models.CharField(max_length=100, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(Tag, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f" {self.pk} {self.title}"

    class Meta:
        ordering = ["-date_published"]
