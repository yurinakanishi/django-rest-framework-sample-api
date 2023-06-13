from django.urls import path, include
from rest_framework.routers import DefaultRouter
from general.views import (
    GenreList,
    GenreCreate,
    GenreDetail,
    TagList,
    TagCreate,
    TagDetail,
)

urlpatterns = [
    path("genres", GenreList.as_view(), name="genre-list"),
    path("genre/<slug:name>/", GenreDetail.as_view(), name="genre-detail"),
    path("genre/<slug:name>/create", GenreCreate.as_view(), name="genre-create"),
    path("tags", TagList.as_view(), name="tag-list"),
    path("tag/<slug:name>/", TagDetail.as_view(), name="tag-detail"),
    path("tag/<slug:name>/create", TagCreate.as_view(), name="tag-create"),
]
