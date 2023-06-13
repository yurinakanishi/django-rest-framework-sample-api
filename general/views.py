from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Article, Tag, Genre
from .serializers import (
    ArticleSerializer,
    GenreSerializer,
    TagSerializer,
)

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from api.permissions import IsAdminOrReadOnly, IsCreateUserOrReadOnly


class GenreList(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminOrReadOnly]


class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = "name"
    permission_classes = [IsAdminOrReadOnly]


class GenreCreate(generics.CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = "name"
    permission_classes = [IsAdminOrReadOnly]


class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminOrReadOnly]


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "name"
    permission_classes = [IsAdminOrReadOnly]


class TagCreate(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "name"
    permission_classes = [IsAdminOrReadOnly]
