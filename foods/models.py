from django.db import models
from django.utils import timezone
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from general.models import Article, Tag, Genre


class CookingMethod(models.Model):
    name = models.CharField(max_length=200)
    name_jp = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    genre = models.ManyToManyField(Genre, related_name="cooking_methods")
    tag = models.ManyToManyField(Tag, related_name="cooking_methods")

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    FOOD_TYPE_CHOICES = [
        ("FT", "Fruit"),
        ("VG", "Vegetable"),
        ("MT", "Meat"),
        ("DY", "Dairy"),
        ("GR", "Grain"),
        ("EG", "Eggs"),
        ("FS", "Fish"),
        ("SH", "Shellfish"),
        ("SW", "Sweets"),
        ("BV", "Beverages"),
        ("NK", "Nuts and Seeds"),
        ("LG", "Legumes"),
        ("OL", "Oils"),
        ("SP", "Spices"),
        ("HR", "Herbs"),
        ("PL", "Poultry"),
        ("FD", "Fast Food"),
        ("PS", "Processed Food"),
    ]
    name = models.CharField(max_length=200, choices=FOOD_TYPE_CHOICES)
    name_jp = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    genre = models.ManyToManyField(Genre, related_name="ingredients")
    tag = models.ManyToManyField(Tag, related_name="ingredients")

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=200)
    name_jp = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    ingredients = models.ManyToManyField("Ingredient", related_name="foods")
    cooking_method = models.ForeignKey(CookingMethod, on_delete=models.CASCADE)
    calories = models.IntegerField()
    description = models.TextField()
    article = models.OneToOneField(Article, on_delete=models.CASCADE, null=True)
    genre = models.ManyToManyField(Genre, related_name="foods")
    tag = models.ManyToManyField(Tag, related_name="foods")

    def __str__(self):
        return self.name
