from django.urls import path, include
from rest_framework.routers import DefaultRouter

from arts.views import (
    ArtsEachList,
    ArtsEachDetail,
    ArtsEachCreate,
    PaintingMethodList,
    PaintingMethodDetail,
    PaintingMethodCreate,
    PaintingStyleList,
    PaintingStyleDetail,
    PaintingStyleCreate,
    ArtsPeriodCreate,
    ArtsPeriodDetail,
    ArtsPeriodList,
    ArtistDetail,
    ArtistCreate,
)

urlpatterns = [
    path("each/", ArtsEachList.as_view(), name="arts-each-list"),
    path("each/<slug:slug>/", ArtsEachDetail.as_view(), name="arts-each-detail"),
    path(
        "each/create/",
        ArtsEachCreate.as_view(),
        name="arts-each-create",
    ),
    path("painting-methods/", PaintingMethodList.as_view(), name="arts-methods-list"),
    path(
        "painting-methods/<slug:slug>/",
        PaintingMethodDetail.as_view(),
        name="arts-method-detail",
    ),
    path(
        "painting-methods/create/",
        PaintingMethodCreate.as_view(),
        name="arts-method-create",
    ),
    path(
        "painting-styles/",
        PaintingStyleList.as_view(),
        name="arts-painting-styles-list",
    ),
    path(
        "painting-styles/<slug:slug>/",
        PaintingStyleDetail.as_view(),
        name="arts-painting-style-detail",
    ),
    path(
        "painting-styles/create/",
        PaintingStyleCreate.as_view(),
        name="arts-painting-style-create",
    ),
    path("period", ArtsPeriodList.as_view(), name="arts-periods-list"),
    path(
        "period/<slug:slug>/",
        ArtsPeriodDetail.as_view(),
        name="arts-period-detail",
    ),
    path(
        "period/create",
        ArtsPeriodCreate.as_view(),
        name="arts-period-create",
    ),
]
