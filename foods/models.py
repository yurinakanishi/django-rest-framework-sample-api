from django.db import models
from django.utils import timezone
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from general.models import Article, Tag, Genre
from locations.models import Location


class CookingMethod(models.Model):
    METHOD_CHOICES = [
        ("stew", "Stew", "シチュー"),
        ("deep_fried", "Deep Fried", "揚げ物"),
    ]
    name = [en for _, en, _ in METHOD_CHOICES]
    name_jp = [jp for _, _, jp in METHOD_CHOICES]
    slug = models.SlugField(max_length=200, blank=True)
    excerpt = models.TextField(max_length=200, default="")
    excerpt_jp = models.TextField(max_length=200, default="")
    description = models.TextField()
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    genres = models.ManyToManyField(Genre, related_name="cooking_methods")
    tags = models.ManyToManyField(Tag, related_name="cooking_methods")

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    TYPE_CHOICES = [
        ("fruits", "Fruits", "果物"),
        ("vegetables", "Vegetables", "野菜"),
        ("meats", "Meats", "肉"),
        ("dairy_products", "Dairy Products", "乳製品"),
        ("grains", "Grains", "穀物"),
        ("eggs", "Eggs", "卵"),
        ("fish", "Fish", "魚"),
        ("beans", "Beans", "豆"),
    ]
    name = [en for _, en, _ in TYPE_CHOICES]
    name_jp = [jp for _, _, jp in TYPE_CHOICES]
    slug = models.SlugField(max_length=200, blank=True)
    excerpt = models.TextField(max_length=200, default="")
    excerpt_jp = models.TextField(max_length=200, default="")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    genres = models.ManyToManyField(Genre, related_name="ingredients")
    tags = models.ManyToManyField(Tag, related_name="ingredients")

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100)
    name_jp = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    excerpt = models.TextField(max_length=200, default="")
    excerpt_jp = models.TextField(max_length=200, default="")
    ingredients = models.ManyToManyField("Ingredient", related_name="foods")
    cooking_method = models.ForeignKey(CookingMethod, on_delete=models.CASCADE)
    calories = models.IntegerField()
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    genres = models.ManyToManyField(Genre, related_name="foods")
    tags = models.ManyToManyField(Tag, related_name="foods")

    def __str__(self):
        return self.name
