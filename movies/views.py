from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Movie, MovieRating, MovieActor
from .serializers import (
    MovieActorSerializerForCreateUpdate,
    MovieActorSerializerForGet,
    MovieActorSerializerForDestroy,
    MovieRatingSerializerForCreateUpdate,
    MovieRatingSerializerForGet,
    MovieRatingSerializerForDestroy,
    MovieSerializerForCreateUpdate,
    MovieSerializerForGet,
    MovieSerializerForDestroy,
    MovieActorSerializerForGet,
    MovieActorSerializerForCreateUpdate,
    MovieActorSerializerForDestroy,
    MovieSearchSerializer,
)
from accounts.permissions import IsAdminOrReadOnly, IsCreateUserOrReadOnly
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
    IsAuthenticated,
    AllowAny,
)


class MovieSearchList(generics.ListAPIView):
    serializer_class = MovieSearchSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_language_queryset(self):
        lang = self.request.GET.get("lang", "en")
        return Movie.objects.filter(language__name=lang)


class BaseMovieList(generics.ListAPIView):
    serializer_class = MovieSerializerForGet
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]

    def get_language_queryset(self):
        lang = self.request.GET.get("lang", "en")
        return Movie.objects.filter(language__name=lang)


class MovieListWithPagination(BaseMovieList):
    paginate_by = 30

    def get_queryset(self):
        return self.get_language_queryset()


class MovieList(BaseMovieList):
    def get_queryset(self):
        return self.get_language_queryset()


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializerForGet
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]


class MovieCreate(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsAuthenticated]


class MovieUpdate(generics.UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializerForCreateUpdate
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]


class MovieDestroy(generics.DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializerForDestroy
    lookup_field = "slug"
    permission_classes = [IsCreateUserOrReadOnly]


class MovieActorList(generics.ListCreateAPIView):
    queryset = MovieActor.objects.all()
    serializer_class = MovieActorSerializerForGet


class MovieActorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieActor.objects.all()
    serializer_class = MovieActorSerializerForGet
    lookup_field = "id"


class MovieActorCreate(generics.CreateAPIView):
    queryset = MovieActor.objects.all()
    serializer_class = MovieActorSerializerForCreateUpdate


class MovieActorUpdate(generics.UpdateAPIView):
    queryset = MovieActor.objects.all()
    serializer_class = MovieActorSerializerForCreateUpdate
    lookup_field = "id"
    permission_classes = [IsCreateUserOrReadOnly]


class MovieActorDestroy(generics.DestroyAPIView):
    queryset = MovieActor.objects.all()
    serializer_class = MovieActorSerializerForDestroy
    lookup_field = "id"
    permission_classes = [IsCreateUserOrReadOnly]


class MovieRatingList(generics.ListCreateAPIView):
    queryset = MovieRating.objects.all()
    serializer_class = MovieRatingSerializerForGet


class MovieRatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieRating.objects.all()
    serializer_class = MovieRatingSerializerForGet
    lookup_field = "id"


class MovieRatingCreate(generics.CreateAPIView):
    queryset = MovieRating.objects.all()
    serializer_class = MovieRatingSerializerForCreateUpdate


class MovieRatingUpdate(generics.UpdateAPIView):
    queryset = MovieRating.objects.all()
    serializer_class = MovieRatingSerializerForCreateUpdate
    lookup_field = "id"
    permission_classes = [IsCreateUserOrReadOnly]


class MovieRatingDestroy(generics.DestroyAPIView):
    queryset = MovieRating.objects.all()
    serializer_class = MovieRatingSerializerForDestroy
    lookup_field = "id"
    permission_classes = [IsCreateUserOrReadOnly]
