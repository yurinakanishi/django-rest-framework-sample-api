from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from general.models import Article, Tag, GenreForUrl
from .serializers import CountrySerializer
from accounts.permissions import IsAdminOrReadOnly, IsCreateUserOrReadOnly
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from .models import Country
from .serializers import (
    CountrySerializerForGet,
    CountrySerializerForCreateUpdate,
    CountrySerializerForDestroy,
    CountrySearchSerializer,
)


class CountrySearchList(generics.ListAPIView):
    serializer_class = CountrySearchSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_language_queryset(self):
        lang = self.request.GET.get("lang", "en")
        return Country.objects.filter(language__name=lang)


class CountryList(generics.ListAPIView):
    queryset = Country.objects.filter(language__name="en")
    serializer_class = CountrySerializerForGet
    permission_classes = [IsAdminOrReadOnly]


class CountryListJp(generics.ListAPIView):
    queryset = Country.objects.filter(language__name="jp")
    serializer_class = CountrySerializerForGet
    permission_classes = [IsAdminOrReadOnly]


class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializerForGet
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class CountryCreate(generics.CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsAuthenticated]


class CountryUpdate(generics.UpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]


class CountryDestroy(generics.DestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializerForDestroy
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]
