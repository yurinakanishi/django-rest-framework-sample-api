from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from general.models import Article, Tag, Genre


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
        max_length=100,
        choices=PERIOD_CHOICES,
    )
    slug = models.SlugField(max_length=100, unique=True, blank=True, editable=False)
    name_jp = models.CharField(max_length=100, unique=True)
    excerpt = models.TextField(max_length=200, default="")
    excerpt_jp = models.TextField(max_length=200, default="")
    article = models.OneToOneField(
        Article, on_delete=models.SET_NULL, null=True, blank=True
    )
    genres = models.ManyToManyField(Genre, related_name="period_genres")
    tags = models.ManyToManyField(Tag, related_name="period_tags")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("period_detail", args=[str(self.id)])

    class Meta:
        ordering = ["name"]


class Date(models.Model):
    date = models.DateField()
    period = models.ForeignKey(Period, on_delete=models.CASCADE, related_name="dates")

    def __str__(self):
        return str(self.date)
