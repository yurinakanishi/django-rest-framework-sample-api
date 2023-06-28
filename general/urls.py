from django.urls import path, include
from rest_framework.routers import DefaultRouter
from general.views import (
    GenreList,
    GenreCreate,
    GenreDetail,
    TagList,
    TagCreate,
    TagDetail,
    ArticleList,
    ArticleDetail,
    ArticleCreate,
)
from general.views import genres_bulk_create

urlpatterns = [
    path("genres/bulk-create/", genres_bulk_create, name="genres-bulk-create"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/create/", GenreCreate.as_view(), name="genre-create"),
    path("genres/<slug:slug>/", GenreDetail.as_view(), name="genre-detail"),
    path("tags", TagList.as_view(), name="tag-list"),
    path("tags/<slug:slug>/", TagDetail.as_view(), name="tag-detail"),
    path("tags/create/", TagCreate.as_view(), name="tag-create"),
    path("articles/", ArticleList.as_view(), name="article-list"),
    path("articles/create/", ArticleCreate.as_view(), name="article-create"),
    path("articles/<slug:slug>/", ArticleDetail.as_view(), name="article-detail"),
]
