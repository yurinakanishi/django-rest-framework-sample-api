from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movies.views import (
    MovieList,
    MovieDetail,
    MovieCreate,
    MovieUpdate,
    MovieDestroy,
    MovieListWithPagination,
    MovieSearchList,
)

urlpatterns = [
    # Movie URLs
    path(
        "each/with-pagination/",
        MovieListWithPagination.as_view(),
        name="movie-list-with-pagination",
    ),
    path("each/all/", MovieList.as_view(), name="movie-list"),
    path("each/search/", MovieSearchList.as_view(), name="movie-search"),
    path("each/create/", MovieCreate.as_view(), name="movie-create"),
    path("each/<slug:slug>/", MovieDetail.as_view(), name="movie-detail"),
    path("each/<slug:slug>/update/", MovieUpdate.as_view(), name="movie-update"),
    path("each/<slug:slug>/destroy/", MovieDestroy.as_view(), name="movie-destroy"),
]
