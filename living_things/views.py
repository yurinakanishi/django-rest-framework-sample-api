from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from general.models import Article, Tag, GenreForUrl
from .serializers import (
    LivingThingsSerializerForGet,
    LivingThingsSerializerForCreateUpdate,
    LivingThingsSerializerForDestroy,
    SpeciesSerializerForGet,
    SpeciesSerializerForCreateUpdate,
    SpeciesSerializerForDestroy,
    HabitatSerializerForGet,
    HabitatSerializerForCreateUpdate,
    HabitatSerializerForDestroy,
    LivingThingsSearchSerializer,
)
from locations.serializers import CountrySerializer
from locations.models import Country
from .models import LivingThings, Species, Habitat

from accounts.permissions import IsAdminOrReadOnly, IsCreateUserOrReadOnly
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)


class LivingThingsSearchList(generics.ListAPIView):
    serializer_class = LivingThingsSearchSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_language_queryset(self):
        lang = self.request.GET.get("lang", "en")
        return LivingThings.objects.filter(language__name=lang)


class LivingThingsEachList(generics.ListAPIView):
    serializer_class = LivingThingsSerializerForGet
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        lang = self.request.GET.get("lang", "en")
        return LivingThings.objects.filter(language__name=lang)


class LivingThingsEachDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LivingThings.objects.all()
    serializer_class = LivingThingsSerializerForGet
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class LivingThingsEachCreate(generics.CreateAPIView):
    queryset = LivingThings.objects.all()
    serializer_class = LivingThingsSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsAuthenticated]


class LivingThingsEachUpdate(generics.UpdateAPIView):
    queryset = LivingThings.objects.all()
    serializer_class = LivingThingsSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]


class LivingThingsEachDestroy(generics.DestroyAPIView):
    queryset = LivingThings.objects.all()
    serializer_class = LivingThingsSerializerForDestroy
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]


# ============================================================


class LivingThingsSpecieList(generics.ListAPIView):
    serializer_class = SpeciesSerializerForGet
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        lang = self.request.GET.get("lang")
        if lang:
            return Species.objects.filter(language__name=lang)
        return Species.objects.all()


class LivingThingsSpecieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializerForGet
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class LivingThingsSpecieCreate(generics.CreateAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsAuthenticated]


class LivingThingsSpecieUpdate(generics.UpdateAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]


class LivingThingsSpecieDestroy(generics.DestroyAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializerForDestroy
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]


# ============================================================


# class LivingThingsCountryList(generics.ListAPIView):
#     queryset = Country.objects.all()
#     serializer_class = CountrySerializerForGet
#     permission_classes = [IsAdminOrReadOnly]


# class LivingThingsCountryDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Country.objects.all()
#     serializer_class = CountrySerializerForGet
#     lookup_field = "slug"
#     permission_classes = [IsAdminOrReadOnly]


# class LivingThingsCountryCreate(generics.CreateAPIView):
#     queryset = Country.objects.all()
#     serializer_class = CountrySerializerForCreateUpdate
#     lookup_field = "slug"
#     permission_classes = [IsAuthenticated]


# class LivingThingsCountryUpdate(generics.UpdateAPIView):
#     queryset = Country.objects.all()
#     serializer_class = CountrySerializerForCreateUpdate
#     lookup_field = "slug"
#     permission_classes = [IsCreateUserOrReadOnly]


# class LivingThingsCountryDestroy(generics.DestroyAPIView):
#     queryset = Country.objects.all()
#     serializer_class = CountrySerializerForDestroy
#     lookup_field = "slug"
#     permission_classes = [IsCreateUserOrReadOnly]

# ============================================================


class LivingThingsHabitatList(generics.ListAPIView):
    serializer_class = HabitatSerializerForGet
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        lang = self.request.GET.get("lang")
        if lang:
            return Habitat.objects.filter(language__name=lang)
        return Habitat.objects.all()


class LivingThingsHabitatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habitat.objects.all()
    serializer_class = HabitatSerializerForGet
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class LivingThingsHabitatCreate(generics.CreateAPIView):
    queryset = Habitat.objects.all()
    serializer_class = HabitatSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsAuthenticated]


class LivingThingsHabitatUpdate(generics.UpdateAPIView):
    queryset = Habitat.objects.all()
    serializer_class = HabitatSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]


class LivingThingsHabitatDestroy(generics.DestroyAPIView):
    queryset = Habitat.objects.all()
    serializer_class = HabitatSerializerForDestroy
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]
