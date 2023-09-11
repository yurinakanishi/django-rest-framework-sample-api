from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from general.models import Article, Tag, GenreForUrl
from .models import Art, Artist, Museum, PaintingMethod, PaintingStyle, ArtsPeriod
from .serializers import (
    ArtSerializerForCreateUpdate,
    ArtSerializerForGet,
    ArtSerializerForDestroy,
    PaintingMethodSerializerForCreateUpdate,
    PaintingMethodSerializerForGet,
    PaintingMethodSerializerForDestroy,
    PaintingStyleSerializerForCreateUpdate,
    PaintingStyleSerializerForGet,
    PaintingStyleSerializerForDestroy,
    ArtsPeriodSerializerForCreateUpdate,
    ArtsPeriodSerializerForGet,
    ArtsPeriodSerializerForDestroy,
    MuseumSerializerForCreateUpdate,
    MuseumSerializerForDestroy,
    MuseumSerializerForGet,
    ArtistSerializerForCreateUpdate,
    ArtistSerializerForDestroy,
    ArtistSerializerForGet,
    ArtSearchSerializer,
)
from accounts.permissions import IsAdminOrReadOnly, IsCreateUserOrReadOnly
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser


class ArtSearchList(generics.ListAPIView):
    serializer_class = ArtSearchSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_language_queryset(self):
        lang = self.request.GET.get("lang", "en")
        return Art.objects.filter(language__name=lang)


class ArtEachList(generics.ListAPIView):
    serializer_class = ArtSerializerForGet
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        lang = self.kwargs.get("lang", "en")
        return Art.objects.filter(language__name=lang)


class ArtEachDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Art.objects.all()
    serializer_class = ArtSerializerForGet
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class ArtEachCreate(generics.CreateAPIView):
    queryset = Art.objects.all()
    serializer_class = ArtSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsAuthenticated]


class ArtEachUpdate(generics.UpdateAPIView):
    queryset = Art.objects.all()
    serializer_class = ArtSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]


class ArtEachDestroy(generics.DestroyAPIView):
    queryset = Art.objects.all()
    serializer_class = ArtSerializerForDestroy
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]


# ====================================================================================================


class PaintingMethodList(generics.ListAPIView):
    serializer_class = PaintingMethodSerializerForGet
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        lang = self.kwargs.get("lang", "en")
        return PaintingMethod.objects.filter(language__name=lang)


class PaintingMethodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaintingMethod.objects.all()
    serializer_class = PaintingMethodSerializerForGet
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class PaintingMethodCreate(generics.CreateAPIView):
    queryset = PaintingMethod.objects.all()
    serializer_class = PaintingMethodSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsAuthenticated]


class PaintingMethodUpdate(generics.UpdateAPIView):
    queryset = PaintingMethod.objects.all()
    serializer_class = PaintingMethodSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]


class PaintingMethodDestroy(generics.DestroyAPIView):
    queryset = PaintingMethod.objects.all()
    serializer_class = PaintingMethodSerializerForDestroy
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]


# ====================================================================================================
class PaintingStyleList(generics.ListAPIView):
    serializer_class = PaintingStyleSerializerForGet
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        lang = self.request.GET.get("lang", "en")
        return PaintingStyle.objects.filter(language__name=lang)


class PaintingStyleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaintingStyle.objects.all()
    serializer_class = PaintingStyleSerializerForGet
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class PaintingStyleCreate(generics.CreateAPIView):
    queryset = PaintingStyle.objects.all()
    serializer_class = PaintingStyleSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsAuthenticated]


class PaintingStyleUpdate(generics.UpdateAPIView):
    queryset = PaintingStyle.objects.all()
    serializer_class = PaintingStyleSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]


class PaintingStyleDestroy(generics.DestroyAPIView):
    queryset = PaintingStyle.objects.all()
    serializer_class = PaintingStyleSerializerForDestroy
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]


# ====================================================================================================


class ArtsPeriodList(generics.ListAPIView):
    serializer_class = ArtsPeriodSerializerForGet
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        lang = self.request.GET.get("lang", "en")
        return ArtsPeriod.objects.filter(language__name=lang)


class ArtsPeriodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArtsPeriod.objects.all()
    serializer_class = ArtsPeriodSerializerForGet
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class ArtsPeriodCreate(generics.CreateAPIView):
    queryset = ArtsPeriod.objects.all()
    serializer_class = ArtsPeriodSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsAuthenticated]


class ArtsPeriodUpdate(generics.UpdateAPIView):
    queryset = ArtsPeriod.objects.all()
    serializer_class = ArtsPeriodSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]


class ArtsPeriodDestroy(generics.DestroyAPIView):
    queryset = ArtsPeriod.objects.all()
    serializer_class = ArtsPeriodSerializerForDestroy
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]


# ====================================================================================================


class ArtistList(generics.ListAPIView):
    serializer_class = ArtistSerializerForGet
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        lang = self.request.GET.get("lang", "en")
        return Artist.objects.filter(language__name=lang)


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializerForGet
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class ArtistCreate(generics.CreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsAuthenticated]


class ArtistUpdate(generics.UpdateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]


class ArtistDestroy(generics.DestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializerForDestroy
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]


# ====================================================================================================
class MuseumList(generics.ListAPIView):
    serializer_class = MuseumSerializerForGet
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        lang = self.request.GET.get("lang", "en")
        return Museum.objects.filter(language__name=lang)


class MuseumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Museum.objects.all()
    serializer_class = MuseumSerializerForGet
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class MuseumCreate(generics.CreateAPIView):
    queryset = Museum.objects.all()
    serializer_class = MuseumSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsAuthenticated]


class MuseumUpdate(generics.UpdateAPIView):
    queryset = Museum.objects.all()
    serializer_class = MuseumSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]


class MuseumDestroy(generics.DestroyAPIView):
    queryset = Museum.objects.all()
    serializer_class = MuseumSerializerForDestroy
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]
