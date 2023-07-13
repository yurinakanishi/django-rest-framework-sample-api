from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movies.views import MovieList, MovieDetail, MovieCreate, MovieUpdate, MovieDestroy

urlpatterns = [
    # Movie URLs
    path("", MovieList.as_view(), name="movie-list"),
    path("jp/", MovieList.as_view(), name="jp-movie-list"),
    path("create/", MovieCreate.as_view(), name="movie-create"),
    path("<slug:slug>/", MovieDetail.as_view(), name="movie-detail"),
    path("<slug:slug>/update/", MovieUpdate.as_view(), name="movie-update"),
    path("<slug:slug>/destroy/", MovieDestroy.as_view(), name="movie-destroy"),
]
