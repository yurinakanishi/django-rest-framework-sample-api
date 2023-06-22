from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from general.models import Article, Tag, Genre
from .serializers import (
    FoodSerializer,
    CookingMethodSerializer,
    IngredientsSerializer,
)
from locations.serializers import CountrySerializer
from .models import CookingMethod, Ingredient, Food
from rest_framework.permissions import AllowAny, IsAdminUser, IsAdminUser
from api.permissions import IsAdminOrReadOnly, IsCreateUserOrReadOnly


class FoodEachList(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAdminOrReadOnly]


class FoodEachDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class FoodEachCreate(generics.CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminUser]


class FoodCountryList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAdminOrReadOnly]


class FoodCountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = CountrySerializer
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class FoodCountryCreate(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = CountrySerializer
    lookup_field = "slug"
    permission_classes = [IsAdminUser]


class FoodCookingMethodList(generics.ListAPIView):
    queryset = CookingMethod.objects.all()
    serializer_class = CookingMethodSerializer
    permission_classes = [IsAdminOrReadOnly]


class FoodCookingMethodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CookingMethod.objects.all()
    serializer_class = CookingMethodSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class FoodCookingMethodCreate(generics.CreateAPIView):
    queryset = CookingMethod.objects.all()
    serializer_class = CookingMethodSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminUser]


class FoodIngredientList(generics.ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientsSerializer
    permission_classes = [IsAdminOrReadOnly]


class FoodIngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientsSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class FoodIngredientCreate(generics.CreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientsSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminUser]
