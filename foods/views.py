from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from general.models import Article, Tag, GenreForUrl
from .serializers import (
    FoodSerializerForCreateUpdate,
    FoodSerializerForDestroy,
    FoodSerializerForGet,
    CookingMethodSerializerForCreateUpdate,
    CookingMethodSerializerForDestroy,
    CookingMethodSerializerForGet,
    IngredientsSerializerForCreateUpdate,
    IngredientsSerializerForDestroy,
    IngredientsSerializerForGet,
    FoodSearchSerializer,
)
from locations.serializers import CountrySerializer
from .models import CookingMethod, Ingredient, Food
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAdminUser,
    IsAuthenticated,
)
from accounts.permissions import IsAdminOrReadOnly, IsCreateUserOrReadOnly


class FoodSearchList(generics.ListAPIView):
    serializer_class = FoodSearchSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_language_queryset(self):
        lang = self.request.GET.get("lang", "en")
        return Food.objects.filter(language__name=lang)


class FoodEachList(generics.ListAPIView):
    serializer_class = FoodSerializerForGet
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        lang = self.request.GET.get("lang", "en")
        return Food.objects.filter(language__name=lang)


class FoodEachDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializerForGet
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class FoodEachCreate(generics.CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsAuthenticated]


class FoodEachUpdate(generics.UpdateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]


class FoodEachDestroy(generics.DestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializerForDestroy
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]


# class FoodCountryList(generics.ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = CountrySerializerForGet
#     permission_classes = [IsAdminOrReadOnly]


# class FoodCountryDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = CountrySerializerForGet
#     lookup_field = "slug"
#     permission_classes = [IsAdminOrReadOnly]


# class FoodCountryCreate(generics.CreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = CountrySerializerForCreateUpdate
#     lookup_field = "slug"
#     permission_classes = [IsAuthenticated]


# ====================================================================================================
class CookingMethodList(generics.ListAPIView):
    serializer_class = CookingMethodSerializerForGet
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        lang = self.request.GET.get("lang", "en")
        return CookingMethod.objects.filter(language__name=lang)


class CookingMethodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CookingMethod.objects.all()
    serializer_class = CookingMethodSerializerForGet
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class CookingMethodCreate(generics.CreateAPIView):
    queryset = CookingMethod.objects.all()
    serializer_class = CookingMethodSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsAuthenticated]


class CookingMethodUpdate(generics.UpdateAPIView):
    queryset = CookingMethod.objects.all()
    serializer_class = CookingMethodSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]


class CookingMethodDestroy(generics.DestroyAPIView):
    queryset = CookingMethod.objects.all()
    serializer_class = CookingMethodSerializerForDestroy
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]


# ====================================================================================================
class IngredientList(generics.ListAPIView):
    serializer_class = IngredientsSerializerForGet
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        lang = self.request.GET.get("lang", "en")
        return Ingredient.objects.filter(language__name=lang)


class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientsSerializerForGet
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class IngredientCreate(generics.CreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientsSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsAuthenticated]


class IngredientUpdate(generics.UpdateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientsSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]


class IngredientDestroy(generics.DestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientsSerializerForDestroy
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]
