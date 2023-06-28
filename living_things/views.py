from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from general.models import Article, Tag, GenreForURL
from .serializers import LivingThingsSerializer, SpeciesSerializer, HabitatSerializer
from locations.serializers import CountrySerializer
from locations.models import Country
from .models import LivingThings, Species, Habitat

from api.permissions import IsAdminOrReadOnly, IsCreateUserOrReadOnly
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)


class LivingThingsEachList(generics.ListAPIView):
    queryset = LivingThings.objects.all()
    serializer_class = LivingThingsSerializer
    permission_classes = [IsAdminOrReadOnly]


class LivingThingsEachDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LivingThings.objects.all()
    serializer_class = LivingThingsSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class LivingThingsEachCreate(generics.CreateAPIView):
    queryset = LivingThings.objects.all()
    serializer_class = LivingThingsSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminUser]


class LivingThingsSpecieList(generics.ListAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    permission_classes = [IsAdminOrReadOnly]


class LivingThingsSpecieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class LivingThingsSpecieCreate(generics.CreateAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminUser]


class LivingThingsCountryList(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAdminOrReadOnly]


class LivingThingsCountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class LivingThingsCountryCreate(generics.CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = "slug"
    permission_classes = [IsAdminUser]


class LivingThingsHabitatList(generics.ListAPIView):
    queryset = Habitat.objects.all()
    serializer_class = HabitatSerializer
    permission_classes = [IsAdminOrReadOnly]


class LivingThingsHabitatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habitat.objects.all()
    serializer_class = HabitatSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class LivingThingsHabitatCreate(generics.CreateAPIView):
    queryset = Habitat.objects.all()
    serializer_class = HabitatSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminUser]
