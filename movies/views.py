from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Movie, MovieRating, MovieReview
from .serializers import (
    MovieActorSerializer,
    MovieRatingSerializer,
    MovieSerializer,
    MovieReviewSerializer,
)
from accounts.permissions import IsAdminOrReadOnly, IsCreateUserOrReadOnly
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
    IsAuthenticated,
    AllowAny,
)


class MovieList(generics.ListAPIView):
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


class MovieReviewList(generics.ListCreateAPIView):
    queryset = MovieReview.objects.all()
    serializer_class = MovieReviewSerializer


class MovieReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieReview.objects.all()
    serializer_class = MovieReviewSerializer
    lookup_field = "id"


class MovieReviewCreate(generics.CreateAPIView):
    queryset = MovieReview.objects.all()
    serializer_class = MovieReviewSerializer
