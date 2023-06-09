from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from articles.models import Article, Tag, Genre
from .serializers import (
    ArticleSerializer,
    GenreSerializer,
    TagSerializer,
)
from .permissions import AdminOrReadOnly
from rest_framework.permissions import AllowAny


class KnowledgeList(generics.ListAPIView):
    queryset = Article.objects.filter(genres__name="knowledge")
    serializer_class = ArticleSerializer


class KnowledgeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(genres__name="knowledge")
    serializer_class = ArticleSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class KnowledgeCreate(generics.CreateAPIView):
    queryset = Article.objects.filter(genres__name="knowledge")
    serializer_class = ArticleSerializer
    lookup_field = "slug"


class ArtsEachList(generics.ListAPIView):
    queryset = Article.objects.filter(genres__name="arts").filter(genres__name="each")
    serializer_class = ArticleSerializer


class ArtsEachDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(genres__name="arts").filter(genres__name="each")
    serializer_class = ArticleSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class ArtsEachCreate(generics.CreateAPIView):
    queryset = Article.objects.filter(genres__name="arts").filter(genres__name="each")
    serializer_class = ArticleSerializer
    lookup_field = "slug"


class ArtsMethodList(generics.ListAPIView):
    queryset = Article.objects.filter(genres__name="arts").filter(
        genres__name="methods"
    )
    serializer_class = ArticleSerializer


class ArtsMethodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(genres__name="arts").filter(
        genres__name="methods"
    )
    serializer_class = ArticleSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class ArtsMethodCreate(generics.CreateAPIView):
    queryset = Article.objects.filter(genres__name="arts").filter(
        genres__name="methods"
    )
    serializer_class = ArticleSerializer
    lookup_field = "slug"


class ArtsPaintingStyleList(generics.ListAPIView):
    queryset = Article.objects.filter(genres__name="arts").filter(
        genres__name="painting-styles"
    )
    serializer_class = ArticleSerializer


class ArtsPaintingStyleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(genres__name="arts").filter(
        genres__name="painting-styles"
    )
    serializer_class = ArticleSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class ArtsPaintingStyleCreate(generics.CreateAPIView):
    queryset = Article.objects.filter(genres__name="arts").filter(
        genres__name="painting-styles"
    )
    serializer_class = ArticleSerializer
    lookup_field = "slug"


class ArtsPeriodList(generics.ListAPIView):
    queryset = Article.objects.filter(genres__name="arts").filter(
        genres__name="periods"
    )
    serializer_class = ArticleSerializer


class ArtsPeriodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(genres__name="arts").filter(
        genres__name="periods"
    )
    serializer_class = ArticleSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class ArtsPeriodCreate(generics.CreateAPIView):
    queryset = Article.objects.filter(genres__name="arts").filter(
        genres__name="periods"
    )
    serializer_class = ArticleSerializer
    lookup_field = "slug"


class LivingThingsEachList(generics.ListAPIView):
    queryset = Article.objects.filter(genres__name="living-things").filter(
        genres__name="each"
    )
    serializer_class = ArticleSerializer


class LivingThingsEachDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(genres__name="living-things").filter(
        genres__name="each"
    )
    serializer_class = ArticleSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class LivingThingsEachCreate(generics.CreateAPIView):
    queryset = Article.objects.filter(genres__name="living-things").filter(
        genres__name="each"
    )
    serializer_class = ArticleSerializer
    lookup_field = "slug"


class LivingThingsSpecieList(generics.ListAPIView):
    queryset = Article.objects.filter(genres__name="living-things").filter(
        genres__name="species"
    )
    serializer_class = ArticleSerializer


class LivingThingsSpecieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(genres__name="living-things").filter(
        genres__name="species"
    )
    serializer_class = ArticleSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class LivingThingsSpecieCreate(generics.CreateAPIView):
    queryset = Article.objects.filter(genres__name="living-things").filter(
        genres__name="species"
    )
    serializer_class = ArticleSerializer
    lookup_field = "slug"


class LivingThingsCountryList(generics.ListAPIView):
    queryset = Article.objects.filter(genres__name="living-things").filter(
        genres__name="countries"
    )
    serializer_class = ArticleSerializer


class LivingThingsCountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(genres__name="living-things").filter(
        genres__name="countries"
    )
    serializer_class = ArticleSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class LivingThingsCountryCreate(generics.CreateAPIView):
    queryset = Article.objects.filter(genres__name="living-things").filter(
        genres__name="countries"
    )
    serializer_class = ArticleSerializer
    lookup_field = "slug"


class LivingThingsHabitatList(generics.ListAPIView):
    queryset = Article.objects.filter(genres__name="living-things").filter(
        genres__name="habitats"
    )
    serializer_class = ArticleSerializer


class LivingThingsHabitatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(genres__name="living-things").filter(
        genres__name="habitats"
    )
    serializer_class = ArticleSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class LivingThingsHabitatCreate(generics.CreateAPIView):
    queryset = Article.objects.filter(genres__name="living-things").filter(
        genres__name="habitats"
    )
    serializer_class = ArticleSerializer
    lookup_field = "slug"


class FoodEachList(generics.ListAPIView):
    queryset = Article.objects.filter(genres__name="food").filter(genres__name="each")
    serializer_class = ArticleSerializer


class FoodEachDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(genres__name="food").filter(genres__name="each")
    serializer_class = ArticleSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class FoodEachCreate(generics.CreateAPIView):
    queryset = Article.objects.filter(genres__name="food").filter(genres__name="each")
    serializer_class = ArticleSerializer
    lookup_field = "slug"


class FoodCountryList(generics.ListAPIView):
    queryset = Article.objects.filter(genres__name="food").filter(
        genres__name="countries"
    )
    serializer_class = ArticleSerializer


class FoodCountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(genres__name="food").filter(
        genres__name="countries"
    )
    serializer_class = ArticleSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class FoodCountryCreate(generics.CreateAPIView):
    queryset = Article.objects.filter(genres__name="food").filter(
        genres__name="countries"
    )
    serializer_class = ArticleSerializer
    lookup_field = "slug"


class FoodMethodList(generics.ListAPIView):
    queryset = Article.objects.filter(genres__name="food").filter(
        genres__name="methods"
    )
    serializer_class = ArticleSerializer


class FoodMethodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(genres__name="food").filter(
        genres__name="methods"
    )
    serializer_class = ArticleSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class FoodMethodCreate(generics.CreateAPIView):
    queryset = Article.objects.filter(genres__name="food").filter(
        genres__name="methods"
    )
    serializer_class = ArticleSerializer
    lookup_field = "slug"


class FoodIngredientList(generics.ListAPIView):
    queryset = Article.objects.filter(genres__name="food").filter(
        genres__name="ingredient"
    )
    serializer_class = ArticleSerializer


class FoodIngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(genres__name="food").filter(
        genres__name="ingredient"
    )
    serializer_class = ArticleSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class FoodCookingCreate(generics.CreateAPIView):
    queryset = Article.objects.filter(genres__name="food").filter(
        genres__name="cooking"
    )
    serializer_class = ArticleSerializer
    lookup_field = "slug"


class FoodCookingList(generics.ListAPIView):
    queryset = Article.objects.filter(genres__name="food").filter(
        genres__name="cooking"
    )
    serializer_class = ArticleSerializer


class FoodCookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(genres__name="food").filter(
        genres__name="cooking"
    )
    serializer_class = ArticleSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class FoodIngredientCreate(generics.CreateAPIView):
    queryset = Article.objects.filter(genres__name="food").filter(
        genres__name="ingredient"
    )
    serializer_class = ArticleSerializer
    lookup_field = "slug"


class MovieList(generics.CreateAPIView):
    queryset = Article.objects.filter(genres__name="movies")
    serializer_class = ArticleSerializer
    lookup_field = "slug"


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(genres__name="movies")
    serializer_class = ArticleSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class MovieCreate(generics.CreateAPIView):
    queryset = Article.objects.filter(genres__name="movies")
    serializer_class = ArticleSerializer
    lookup_field = "slug"


class CountryList(generics.ListAPIView):
    queryset = Article.objects.filter(genres__name="countries")
    serializer_class = ArticleSerializer


class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(genres__name="countries")
    serializer_class = ArticleSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class CountryCreate(generics.CreateAPIView):
    queryset = Article.objects.filter(genres__name="countries")
    serializer_class = ArticleSerializer
    lookup_field = "slug"


class BlogList(generics.ListAPIView):
    queryset = Article.objects.filter(genres__name="blogs")
    serializer_class = ArticleSerializer


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(genres__name="blogs")
    serializer_class = ArticleSerializer
    lookup_field = "slug"


class BlogCreate(generics.CreateAPIView):
    queryset = Article.objects.filter(genres__name="blogs")
    serializer_class = ArticleSerializer
    lookup_field = "slug"


class GenreList(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = "name"
    permission_classes = [AllowAny]


class GenreCreate(generics.CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = "name"


class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "name"
    permission_classes = [AllowAny]


class TagCreate(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "name"
