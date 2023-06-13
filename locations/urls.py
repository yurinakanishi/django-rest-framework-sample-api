from django.urls import path, include
from rest_framework.routers import DefaultRouter
from locations.views import (
    CountryList,
    CountryDetail,
    CountryCreate,
)

urlpatterns = [
    path("countries", CountryList.as_view(), name="country-list"),
    path("country/<slug:slug>/", CountryDetail.as_view(), name="country-detail"),
    path("country/<slug:slug>/create", CountryCreate.as_view(), name="country-create"),
]
