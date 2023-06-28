from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from general.models import Article, Tag, GenreForURL, Language


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
    slug = models.SlugField(max_length=100, unique=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    article = models.OneToOneField(
        Article, on_delete=models.SET_NULL, null=True, blank=True
    )
    genre_for_url = models.ForeignKey(
        GenreForURL,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="period_genre_for_url",
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="period_tags")
    date = models.ManyToManyField(Date, blank=True, related_name="period_dates")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
