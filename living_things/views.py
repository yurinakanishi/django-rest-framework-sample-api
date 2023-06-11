from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from general.models import Article, Tag, Genre
from .serializers import LivingThingsSerializer, SpeciesSerializer, HabitatSerializer
from countries.serializers import CountrySerializer
from countries.models import Country
from .models import LivingThings, Species, Habitat

from api.permissions import AdminOrReadOnly
from rest_framework.permissions import AllowAny


class LivingThingsEachList(generics.ListAPIView):
    queryset = LivingThings.objects.all()
    serializer_class = LivingThingsSerializer


class LivingThingsEachDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LivingThings.objects.all()
    serializer_class = LivingThingsSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class LivingThingsEachCreate(generics.CreateAPIView):
    queryset = LivingThings.objects.all()
    serializer_class = LivingThingsSerializer
    lookup_field = "slug"


class LivingThingsSpecieList(generics.ListAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer


class LivingThingsSpecieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class LivingThingsSpecieCreate(generics.CreateAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    lookup_field = "slug"


class LivingThingsCountryList(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class LivingThingsCountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class LivingThingsCountryCreate(generics.CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = "slug"


class LivingThingsHabitatList(generics.ListAPIView):
    queryset = Habitat.objects.all()
    serializer_class = HabitatSerializer


class LivingThingsHabitatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habitat.objects.all()
    serializer_class = HabitatSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class LivingThingsHabitatCreate(generics.CreateAPIView):
    queryset = Habitat.objects.all()
    serializer_class = HabitatSerializer
    lookup_field = "slug"
