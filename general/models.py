from django.db import models
from django.utils import timezone
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class GenreForUrl(models.Model):
    NAME_CHOICES = [
        ("knowledge/each", "knowledge/each"),
        ("knowledge/blogs", "knowledge/blogs"),
        ("knowledge/test", "knowledge/test"),
        ("movies/each", "movies/each"),
        ("movies/tvs", "movies/tvs"),
        ("arts/each", "arts/each"),
        ("arts/painting-methods", "arts/painting-methods"),
        ("arts/painting-styles", "arts/painting-styles"),
        ("arts/periods", "arts/periods"),
        ("living-things/each", "living-things/each"),
        ("living-things/species", "living-things/species"),
        ("living-things/habitats", "living-things/habitats"),
        ("foods/cooking-methods", "foods/cooking-methods"),
        ("foods/ingredients", "foods/ingredients"),
        ("countries/each", "countries/each"),
    ]
    name = models.CharField(max_length=100, unique=True, choices=NAME_CHOICES)

    NAME_JP_CHOICES = [
        ("知識/それぞれ", "知識/それぞれ"),
        ("知識/ブログ", "知識/ブログ"),
        ("知識/テスト", "知識/テスト"),
        ("映画/それぞれ", "映画/それぞれ"),
        ("映画/TV", "映画/TV"),
        ("芸術/作品", "芸術/作品"),
        ("芸術/絵画手法", "芸術/絵画手法"),
        ("芸術/絵画スタイル", "芸術/絵画スタイル"),
        ("芸術/時代", "芸術/時代"),
        ("生き物/生き物", "生き物/生き物"),
        ("生き物/種族", "生き物/種族"),
        ("生き物/生息地", "生き物/生息地"),
        ("食べ物/調理法", "食べ物/調理法"),
        ("食べ物/材料", "食べ物/材料"),
        ("国", "国"),
    ]
    name_jp = models.CharField(max_length=100, unique=True, choices=NAME_JP_CHOICES)

    def __str__(self):
        return self.name


class Article(models.Model):
    excerpt = models.TextField(max_length=200, blank=True)
    kicker = models.CharField(max_length=100, blank=True)
    content = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    rating = models.FloatField(default=0.0)
    rating_count = models.IntegerField(blank=True, null=True)
    published_date = models.DateTimeField(default=timezone.now, blank=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.excerpt

    class Meta:
        ordering = ["-pk"]


class Language(models.Model):
    NAME_CHOICES = [
        ("en", "english"),
        ("jp", "japanese"),
    ]
    name = models.CharField(max_length=100, unique=True, choices=NAME_CHOICES)

    def __str__(self):
        return self.name


class Category(models.Model):
    CATEGORY_CHOICES = [
        ("Movies", "movies"),
        ("Arts", "arts"),
        ("Living-things", "living-things"),
        ("Foods", "foods"),
        ("Countries", "countries"),
    ]

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
