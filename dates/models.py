from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from general.models import Article, Tag, Genre


class Date(models.Model):
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class Period(models.Model):
    PERIOD_CHOICES = [
        ("ancient_times", "Ancient Times"),
        ("500s_1300s", "500s-1300s"),
        ("1400s", "1400s"),
        ("1500s", "1500s"),
        ("1600s", "1600s"),
        ("1700s", "1700s"),
        ("1800s", "1800s"),
        ("1900s", "1900s"),
        ("2000s", "2000s"),
    ]
    name = models.CharField(
        unique=True,
        max_length=100,
        choices=PERIOD_CHOICES,
    )
    name_jp = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=100, blank=True)
    excerpt = models.TextField(max_length=200, blank=True)
    excerpt_jp = models.TextField(max_length=200, blank=True)
    article = models.OneToOneField(
        Article, on_delete=models.SET_NULL, null=True, blank=True
    )
    genres = models.ManyToManyField(Genre, blank=True, related_name="period_genres")
    tags = models.ManyToManyField(Tag, blank=True, related_name="period_tags")
    date = models.ManyToManyField(Date, blank=True, related_name="period_dates")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
