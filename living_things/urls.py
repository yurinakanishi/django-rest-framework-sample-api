from django.urls import path, include
from rest_framework.routers import DefaultRouter

from living_things.views import (
    LivingThingsEachList,
    LivingThingsEachDetail,
    LivingThingsEachCreate,
    LivingThingsEachDestroy,
    LivingThingsEachUpdate,
    LivingThingsHabitatCreate,
    LivingThingsHabitatList,
    LivingThingsHabitatDetail,
    LivingThingsHabitatDestroy,
    LivingThingsHabitatUpdate,
    LivingThingsSpecieCreate,
    LivingThingsSpecieList,
    LivingThingsSpecieDetail,
    LivingThingsSpecieDestroy,
    LivingThingsSpecieUpdate,
    # LivingThingsCountryCreate,
    # LivingThingsCountryList,
    # LivingThingsCountryDetail,
    # LivingThingsCountryDestroy,
    # LivingThingsCountryUpdate,
)

urlpatterns = [
    path("each/", LivingThingsEachList.as_view(), name="living-things-each-list"),
    path(
        "each/create/",
        LivingThingsEachCreate.as_view(),
        name="living-things-each-create",
    ),
    path(
        "each/<slug:slug>/",
        LivingThingsEachDetail.as_view(),
        name="living-things-each-detail",
    ),
    path(
        "each/<slug:slug>/update/",
        LivingThingsEachUpdate.as_view(),
        name="living-things-each-update",
    ),
    path(
        "each/<slug:slug>/destroy/",
        LivingThingsEachDestroy.as_view(),
        name="living-things-each-destroy",
    ),
    path(
        "habitats/",
        LivingThingsHabitatList.as_view(),
        name="living-things-habitat-list",
    ),
    path(
        "habitats/create/",
        LivingThingsHabitatCreate.as_view(),
        name="living-things-habitat-create",
    ),
    path(
        "habitats/<slug:slug>/",
        LivingThingsHabitatDetail.as_view(),
        name="living-things-habitat-detail",
    ),
    path(
        "habitats/<slug:slug>/update/",
        LivingThingsHabitatUpdate.as_view(),
        name="living-things-habitat-update",
    ),
    path(
        "habitats/<slug:slug>/destroy/",
        LivingThingsHabitatDestroy.as_view(),
        name="living-things-habitat-destroy",
    ),
    path(
        "species/", LivingThingsSpecieList.as_view(), name="living-things-specie-list"
    ),
    path(
        "species/create/",
        LivingThingsSpecieCreate.as_view(),
        name="living-things-specie-create",
    ),
    path(
        "species/<slug:slug>/",
        LivingThingsSpecieDetail.as_view(),
        name="living-things-specie-detail",
    ),
    path(
        "species/<slug:slug>/update/",
        LivingThingsSpecieUpdate.as_view(),
        name="living-things-specie-update",
    ),
    path(
        "species/<slug:slug>/destroy/",
        LivingThingsSpecieDestroy.as_view(),
        name="living-things-specie-destroy",
    ),
    # path(
    #     "countries/",
    #     LivingThingsCountryList.as_view(),
    #     name="living-things-country-list",
    # ),
    # path(
    #     "country/create/",
    #     LivingThingsCountryCreate.as_view(),
    #     name="living-things-country-create",
    # ),
    # path(
    #     "country/<slug:slug>/",
    #     LivingThingsCountryDetail.as_view(),
    #     name="living-things-country-detail",
    # ),
    # path(
    #     "country/<slug:slug>/update/",
    #     LivingThingsCountryUpdate.as_view(),
    #     name="living-things-country-update",
    # ),
    # path(
    #     "country/<slug:slug>/destroy/",
    #     LivingThingsCountryDestroy.as_view(),
    #     name="living-things-country-destroy",
    # ),
]
