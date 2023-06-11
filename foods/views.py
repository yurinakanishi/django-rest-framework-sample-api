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
from countries.serializers import CountrySerializer

from api.permissions import AdminOrReadOnly
from rest_framework.permissions import AllowAny


class FoodEachList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = FoodSerializer


class FoodEachDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = FoodSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class FoodEachCreate(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = FoodSerializer
    lookup_field = "slug"


class FoodCountryList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = CountrySerializer


class FoodCountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = CountrySerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class FoodCountryCreate(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = CountrySerializer
    lookup_field = "slug"


class FoodCookingMethodList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = CookingMethodSerializer


class FoodCookingMethodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = CookingMethodSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class FoodCookingMethodCreate(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = CookingMethodSerializer
    lookup_field = "slug"


class FoodIngredientList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = IngredientsSerializer


class FoodIngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = IngredientsSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class FoodIngredientCreate(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = IngredientsSerializer
    lookup_field = "slug"
