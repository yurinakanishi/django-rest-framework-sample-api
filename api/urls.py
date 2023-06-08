from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ArticleList,
    ArticleCreate,
    ArticleDetail,
    GenreList,
    GenreCreate,
    GenreDetail,
    TagList,
    TagCreate,
    TagDetail,
)

urlpatterns = [
    path("articles", ArticleList.as_view(), name="article-list"),
    path(
        "article/<int:pk>/create",
        ArticleCreate.as_view(),
        name="article-create",
    ),
    path("article/<int:pk>/", ArticleDetail.as_view(), name="article-detail"),
    path("genres", GenreList.as_view(), name="genre-list"),
    path("genre/<int:pk>/create", GenreCreate.as_view(), name="genre-create"),
    path("genre/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("tags", TagList.as_view(), name="tag-list"),
    path("tag/<int:pk>/create", TagCreate.as_view(), name="tag-create"),
    path("tag/<int:pk>/", TagDetail.as_view(), name="tag-detail"),
]
