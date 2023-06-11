from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from general.models import Article, Tag, Genre
from .serializers import (
    ArtSerializer,
    PaintingMethodSerializer,
    PaintingStyleSerializer,
    MuseumSerializer,
    ArtistSerializer,
)

from api.permissions import AdminOrReadOnly
from rest_framework.permissions import AllowAny


class ArtsEachList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArtSerializer


class ArtsEachDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArtSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class ArtsEachCreate(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArtSerializer
    lookup_field = "slug"


class ArtsMethodList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = PaintingStyleSerializer


class ArtsMethodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = PaintingStyleSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class ArtsMethodCreate(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = PaintingStyleSerializer
    lookup_field = "slug"


class ArtsPaintingStyleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = PaintingMethodSerializer


class ArtsPaintingStyleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = PaintingMethodSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class ArtsPaintingStyleCreate(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = PaintingMethodSerializer
    lookup_field = "slug"


# class ArtsPeriodList(generics.ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = generalerializer


# class ArtsPeriodDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = generalerializer
#     lookup_field = "slug"
#     permission_classes = [AllowAny]


# class ArtsPeriodCreate(generics.CreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = generalerializer
#     lookup_field = "slug"
