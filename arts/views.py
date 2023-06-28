from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from general.models import Article, Tag, GenreForURL
from .models import Art, Artist, Museum, PaintingMethod, PaintingStyle
from .serializers import (
    ArtSerializer,
    PaintingMethodSerializer,
    PaintingStyleSerializer,
    MuseumSerializer,
    ArtistSerializer,
)
from accounts.permissions import IsAdminOrReadOnly, IsCreateUserOrReadOnly
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser


class ArtsEachList(generics.ListAPIView):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer
    permission_classes = [IsAdminOrReadOnly]


class ArtsEachDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class ArtsEachCreate(generics.CreateAPIView):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminUser]


class PaintingMethodList(generics.ListAPIView):
    queryset = PaintingMethod.objects.all()
    serializer_class = PaintingMethodSerializer
    permission_classes = [IsAdminOrReadOnly]


class PaintingMethodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaintingMethod.objects.all()
    serializer_class = PaintingMethodSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class PaintingMethodCreate(generics.CreateAPIView):
    queryset = PaintingMethod.objects.all()
    serializer_class = PaintingMethodSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminUser]


class PaintingStyleList(generics.ListAPIView):
    queryset = PaintingStyle.objects.all()
    serializer_class = PaintingStyleSerializer
    permission_classes = [IsAdminOrReadOnly]


class PaintingStyleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaintingStyle.objects.all()
    serializer_class = PaintingStyleSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class PaintingStyleCreate(generics.CreateAPIView):
    queryset = PaintingStyle.objects.all()
    serializer_class = PaintingStyleSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminUser]


# class ArtsPeriodList(generics.ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArtPeriodSerializer
#     permission_classes = [IsAdminOrReadOnly]


# class ArtsPeriodDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArtPeriodSerializer
#     lookup_field = "slug"
#     permission_classes = [IsAdminOrReadOnly]


# class ArtsPeriodCreate(generics.CreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArtPeriodSerializer
#     lookup_field = "slug"
#     permission_classes = [IsAdminUser]


class ArtistList(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAdminOrReadOnly]


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class ArtistCreate(generics.CreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminUser]


class MuseumList(generics.ListAPIView):
    queryset = Museum.objects.all()
    serializer_class = MuseumSerializer
    permission_classes = [IsAdminOrReadOnly]


class MuseumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Museum.objects.all()
    serializer_class = MuseumSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class MuseumCreate(generics.CreateAPIView):
    queryset = Museum.objects.all()
    serializer_class = MuseumSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminUser]
