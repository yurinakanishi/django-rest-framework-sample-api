from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Movie, MovieRating
from .serializers import MovieActorSerializer, MovieRatingSerializer, MovieSerializer
from api.permissions import IsAdminOrReadOnly, IsCreateUserOrReadOnly
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
    IsAuthenticated,
    AllowAny,
)


class MovieList(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class MovieCreate(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminUser]


# class MovieActorList(generics.ListCreateAPIView):
#     queryset = MovieActor.objects.all()
#     serializer_class = MovieActorSerializer


# class MovieActorDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = MovieActor.objects.all()
#     serializer_class = MovieActorSerializer
#     lookup_field = "id"


# class MovieActorCreate(generics.CreateAPIView):
#     queryset = MovieActor.objects.all()
#     serializer_class = MovieActorSerializer


class MovieRatingList(generics.ListCreateAPIView):
    queryset = MovieRating.objects.all()
    serializer_class = MovieRatingSerializer


class MovieRatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieRating.objects.all()
    serializer_class = MovieRatingSerializer
    lookup_field = "id"


class MovieRatingCreate(generics.CreateAPIView):
    queryset = MovieRating.objects.all()
    serializer_class = MovieRatingSerializer
