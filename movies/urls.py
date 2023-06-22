from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movies.views import (
    MovieList,
    MovieDetail,
    MovieCreate,
    MovieReviewCreate,
    MovieReviewList,
    MovieReviewDetail,
)

urlpatterns = [
    path("", MovieList.as_view(), name="movie-list"),
    path("<slug:slug>/", MovieDetail.as_view(), name="movie-detail"),
    path("<slug:slug>/create", MovieCreate.as_view(), name="movie-review-create"),
    path("review", MovieReviewList.as_view(), name="movie-list"),
    path(
        "review/<slug:slug>/", MovieReviewDetail.as_view(), name="movie-review-detail"
    ),
    path(
        "review/<slug:slug>/create",
        MovieReviewCreate.as_view(),
        name="movie-review-create",
    ),
]
