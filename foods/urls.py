from django.urls import path, include
from rest_framework.routers import DefaultRouter
from foods.views import (
    FoodEachList,
    FoodEachDetail,
    FoodEachCreate,
    FoodIngredientList,
    FoodIngredientDetail,
    FoodIngredientCreate,
    FoodCookingMethodList,
    FoodCookingMethodDetail,
    FoodCookingMethodCreate,
)

urlpatterns = [
    path("each", FoodEachList.as_view(), name="food-each-list"),
    path("each/<slug:slug>/", FoodEachDetail.as_view(), name="food-each-detail"),
    path(
        "each/create",
        FoodEachCreate.as_view(),
        name="food-each-create",
    ),
    path("ingredients/", FoodIngredientList.as_view(), name="food-ingredients-list"),
    path(
        "ingredients/<slug:slug>/",
        FoodIngredientDetail.as_view(),
        name="food-ingredients-detail",
    ),
    path(
        "ingredients/create",
        FoodIngredientCreate.as_view(),
        name="food-ingredients-create",
    ),
    path("cooking-methods/", FoodCookingMethodList.as_view(), name="food-cooking-list"),
    path(
        "cooking-methods/<slug:slug>/",
        FoodCookingMethodDetail.as_view(),
        name="food-cooking-detail",
    ),
    path(
        "cooking-methods/create",
        FoodCookingMethodCreate.as_view(),
        name="food-cooking-create",
    ),
]
