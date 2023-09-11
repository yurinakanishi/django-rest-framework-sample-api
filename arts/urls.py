from django.urls import path, include
from rest_framework.routers import DefaultRouter

from arts.views import (
    ArtEachList,
    ArtEachCreate,
    ArtEachDetail,
    ArtEachDestroy,
    ArtsPeriodUpdate,
    ArtsPeriodDestroy,
    ArtsPeriodCreate,
    ArtsPeriodDetail,
    ArtsPeriodList,
    PaintingMethodCreate,
    PaintingMethodDetail,
    PaintingMethodList,
    PaintingMethodDestroy,
    PaintingMethodUpdate,
    PaintingStyleCreate,
    PaintingStyleDetail,
    PaintingStyleList,
    PaintingStyleDestroy,
    PaintingStyleUpdate,
    ArtistList,
    ArtistUpdate,
    ArtistDestroy,
    ArtistDetail,
    ArtistCreate,
    ArtSearchList,
)

urlpatterns = [
    path("search/", ArtSearchList.as_view(), name="arts-search"),
    # ArtEach URLs
    path("each/", ArtEachList.as_view(), name="arts-each-list"),
    path("each/create/", ArtEachCreate.as_view(), name="arts-each-create"),
    path("each/<slug:slug>/", ArtEachDetail.as_view(), name="arts-each-detail"),
    path(
        "each/<slug:slug>/destroy/", ArtEachDestroy.as_view(), name="arts-each-destroy"
    ),
    # ArtsPeriod URLs
    path("periods/", ArtsPeriodList.as_view(), name="arts-periods-list"),
    path("periods/create/", ArtsPeriodCreate.as_view(), name="arts-periods-create"),
    path(
        "periods/<slug:slug>/", ArtsPeriodDetail.as_view(), name="arts-periods-detail"
    ),
    path(
        "periods/<slug:slug>/update/",
        ArtsPeriodUpdate.as_view(),
        name="arts-periods-update",
    ),
    path(
        "periods/<slug:slug>/destroy/",
        ArtsPeriodDestroy.as_view(),
        name="arts-period-destroy",
    ),
    # PaintingMethod URLs
    path("painting-methods/", PaintingMethodList.as_view(), name="arts-methods-list"),
    path(
        "painting-methods/create/",
        PaintingMethodCreate.as_view(),
        name="arts-method-create",
    ),
    path(
        "painting-methods/<slug:slug>/",
        PaintingMethodDetail.as_view(),
        name="arts-method-detail",
    ),
    path(
        "painting-methods/<slug:slug>/update/",
        PaintingMethodUpdate.as_view(),
        name="arts-method-update",
    ),
    path(
        "painting-methods/<slug:slug>/destroy/",
        PaintingMethodDestroy.as_view(),
        name="arts-method-destroy",
    ),
    # PaintingStyle URLs
    path(
        "painting-styles/",
        PaintingStyleList.as_view(),
        name="arts-painting-styles-list",
    ),
    path(
        "painting-styles/create/",
        PaintingStyleCreate.as_view(),
        name="arts-painting-style-create",
    ),
    path(
        "painting-styles/<slug:slug>/",
        PaintingStyleDetail.as_view(),
        name="arts-painting-style-detail",
    ),
    path(
        "painting-styles/<slug:slug>/update/",
        PaintingStyleUpdate.as_view(),
        name="arts-painting-style-update",
    ),
    path(
        "painting-styles/<slug:slug>/destroy/",
        PaintingStyleDestroy.as_view(),
        name="arts-painting-style-destroy",
    ),
    path("artists/", ArtistList.as_view(), name="artist-list"),
    path("jp/artists/", ArtistList.as_view(), name="jp-artist-list"),
    path("artists/create/", ArtistCreate.as_view(), name="artist-create"),
    path("artists/<slug:slug>/", ArtistDetail.as_view(), name="artist-detail"),
    path("artists/<slug:slug>/update/", ArtistUpdate.as_view(), name="artist-update"),
    path(
        "artists/<slug:slug>/destroy/", ArtistDestroy.as_view(), name="artist-destroy"
    ),
]
