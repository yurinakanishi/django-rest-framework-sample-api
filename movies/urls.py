from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movies.views import MovieList, MovieDetail, MovieCreate, MovieUpdate, MovieDestroy

urlpatterns = [
    # Movie URLs
    path("movies/", MovieList.as_view(), name="movie-list"),
    path("jp/movies/", MovieList.as_view(), name="jp-movie-list"),
    path("movies/create/", MovieCreate.as_view(), name="movie-create"),
    path("movies/<slug:slug>/", MovieDetail.as_view(), name="movie-detail"),
    path("movies/<slug:slug>/update/", MovieUpdate.as_view(), name="movie-update"),
    path("movies/<slug:slug>/destroy/", MovieDestroy.as_view(), name="movie-destroy"),
]
