from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from articles.models import Article, Tag, Genre
from .serializers import (
    ArticleSerializer,
    GenreSerializer,
    TagSerializer,
)
from django.shortcuts import get_object_or_404


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleListEn(generics.ListAPIView):
    queryset = Article.objects.filter(language="en")
    serializer_class = ArticleSerializer


class ArticleListJa(generics.ListAPIView):
    queryset = Article.objects.filter(language="ja")
    serializer_class = ArticleSerializer


class ArticleCreate(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class GenreList(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreCreate(generics.CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagCreate(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
