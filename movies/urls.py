from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movies.views import (
    MovieList,
    MovieDetail,
    MovieCreate,
)

urlpatterns = [
    path("movies", MovieList.as_view(), name="movie-list"),
    path("movie/<slug:slug>/", MovieDetail.as_view(), name="movie-detail"),
    path("movie/<slug:slug>/create", MovieCreate.as_view(), name="movie-create"),
]
