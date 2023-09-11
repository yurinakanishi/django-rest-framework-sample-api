from django.db import models
from django.utils import timezone
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from general.models import Article, Tag, GenreForUrl, Language
from locations.models import Location


class CookingMethod(models.Model):
    METHOD_CHOICES = [
        ("stew", "Stew"),
        ("deep-fried", "Deep fried"),
        ("シチュー", "Stew jp"),
        ("揚げ物", "Deep fried jp"),
    ]

    name = models.CharField(max_length=200, choices=METHOD_CHOICES)
    slug = models.SlugField(max_length=200, unique=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    article = models.OneToOneField(
        Article, on_delete=models.CASCADE, blank=True, null=True
    )
    genre_for_url = models.ForeignKey(
        GenreForUrl,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="cooking_method_genre_for_url",
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="cooking_method_tags")

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1
    )

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    TYPE_CHOICES = [
        ("fruits", "Fruits"),
        ("vegetables", "Vegetables"),
        ("meats", "Meats"),
        ("dairy_products", "Dairy Products"),
        ("grains", "Grains"),
        ("eggs", "Eggs"),
        ("fish", "Fish"),
        ("beans", "Beans"),
        ("果物", "Fruits jp"),
        ("野菜", "Vegetables jp"),
        ("肉", "Meats jp"),
        ("乳製品", "Dairy Products jp"),
        ("穀物", "Grains jp"),
        ("卵", "Eggs jp"),
        ("魚", "Fish jp"),
        ("豆", "Beans jp"),
    ]

    name = models.CharField(max_length=200, choices=TYPE_CHOICES)
    slug = models.SlugField(max_length=200, unique=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, blank=True, null=True
    )
    article = models.OneToOneField(
        Article, on_delete=models.CASCADE, blank=True, null=True
    )
    genre_for_url = models.ForeignKey(
        GenreForUrl,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="ingredients_genre_for_url",
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="ingredients_tags")

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(
        Ingredient, blank=True, related_name="foods_ingredients"
    )
    cooking_method = models.ForeignKey(
        CookingMethod, on_delete=models.CASCADE, blank=True, null=True
    )
    calories = models.IntegerField()
    article = models.OneToOneField(
        Article, on_delete=models.CASCADE, blank=True, null=True
    )
    genre_for_url = models.ForeignKey(
        GenreForUrl,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="foods_genre_for_url",
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="foods_tags")

    def __str__(self):
        return self.name
