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
    path("foods/each", FoodEachList.as_view(), name="food-each-list"),
    path("foods/each/<slug:slug>/", FoodEachDetail.as_view(), name="food-each-detail"),
    path(
        "foods/each/<slug:slug>/create",
        FoodEachCreate.as_view(),
        name="food-each-create",
    ),
    path(
        "foods/ingredients", FoodIngredientList.as_view(), name="food-ingredients-list"
    ),
    path(
        "foods/ingredients/<slug:slug>/",
        FoodIngredientDetail.as_view(),
        name="food-ingredients-detail",
    ),
    path(
        "foods/ingredients/<slug:slug>/create",
        FoodIngredientCreate.as_view(),
        name="food-ingredients-create",
    ),
    path("foods/cooking", FoodCookingMethodList.as_view(), name="food-cooking-list"),
    path(
        "foods/cooking/<slug:slug>/",
        FoodCookingMethodDetail.as_view(),
        name="food-cooking-detail",
    ),
    path(
        "foods/cooking/<slug:slug>/create",
        FoodCookingMethodCreate.as_view(),
        name="food-cooking-create",
    ),
]
