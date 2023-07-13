from django.urls import path, include
from rest_framework.routers import DefaultRouter
from locations.views import (
    CountryList,
    CountryDetail,
    CountryCreate,
    CountryUpdate,
    CountryDestroy,
)

urlpatterns = [
    path("countries/", CountryList.as_view(), name="country-list"),
    path("countries/create/", CountryCreate.as_view(), name="country-create"),
    path("countries/<slug:slug>/", CountryDetail.as_view(), name="country-detail"),
    path(
        "countries/<slug:slug>/update/", CountryUpdate.as_view(), name="country-update"
    ),
    path(
        "countries/<slug:slug>/destroy/",
        CountryDestroy.as_view(),
        name="country-destroy",
    ),
]
