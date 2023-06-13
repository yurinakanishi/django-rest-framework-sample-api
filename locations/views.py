from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from general.models import Article, Tag, Genre
from .serializers import CountrySerializer
from api.permissions import IsAdminOrReadOnly, IsCreateUserOrReadOnly
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)


class CountryList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAdminOrReadOnly]


class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = CountrySerializer
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class CountryCreate(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = CountrySerializer
    lookup_field = "slug"
    permission_classes = [IsAdminUser]
