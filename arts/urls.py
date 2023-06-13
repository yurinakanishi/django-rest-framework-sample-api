from django.urls import path, include
from rest_framework.routers import DefaultRouter

from arts.views import (
    ArtsEachList,
    ArtsEachDetail,
    ArtsEachCreate,
    ArtsMethodList,
    ArtsMethodDetail,
    ArtsMethodCreate,
    ArtsPaintingStyleList,
    ArtsPaintingStyleDetail,
    ArtsPaintingStyleCreate,
    ArtsPeriodList,
    ArtsPeriodDetail,
    ArtsPeriodCreate,
)

urlpatterns = [
    path("arts/each", ArtsEachList.as_view(), name="arts-each-list"),
    path("arts/each/<slug:slug>/", ArtsEachDetail.as_view(), name="arts-each-detail"),
    path(
        "arts/each/<slug:slug>/create",
        ArtsEachCreate.as_view(),
        name="arts-each-create",
    ),
    path("arts/methods", ArtsMethodList.as_view(), name="arts-methods-list"),
    path(
        "arts/method/<slug:slug>/",
        ArtsMethodDetail.as_view(),
        name="arts-method-detail",
    ),
    path(
        "arts/method/<slug:slug>/create",
        ArtsMethodCreate.as_view(),
        name="arts-method-create",
    ),
    path(
        "arts/painting-styles",
        ArtsPaintingStyleList.as_view(),
        name="arts-painting-styles-list",
    ),
    path(
        "arts/painting-style/<slug:slug>/",
        ArtsPaintingStyleDetail.as_view(),
        name="arts-painting-style-detail",
    ),
    path(
        "arts/painting-style/<slug:slug>/create",
        ArtsPaintingStyleCreate.as_view(),
        name="arts-painting-style-create",
    ),
    path("arts/periods", ArtsPeriodList.as_view(), name="arts-periods-list"),
    path(
        "arts/period/<slug:slug>/",
        ArtsPeriodDetail.as_view(),
        name="arts-period-detail",
    ),
    path(
        "arts/period/<slug:slug>/create",
        ArtsPeriodCreate.as_view(),
        name="arts-period-create",
    ),
]
