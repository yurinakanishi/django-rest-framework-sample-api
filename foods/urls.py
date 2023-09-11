from django.urls import path, include
from rest_framework.routers import DefaultRouter
from foods.views import (
    FoodEachList,
    FoodEachDetail,
    FoodEachCreate,
    FoodEachDestroy,
    FoodEachUpdate,
    IngredientCreate,
    IngredientList,
    IngredientDetail,
    IngredientDestroy,
    IngredientUpdate,
    CookingMethodCreate,
    CookingMethodDestroy,
    CookingMethodDetail,
    CookingMethodList,
    CookingMethodUpdate,
    FoodSearchList,
)

urlpatterns = [
    path("search/", FoodSearchList.as_view(), name="food-search"),
    path("each/", FoodEachList.as_view(), name="food-each-list"),
    path("each/create/", FoodEachCreate.as_view(), name="food-each-create"),
    path("each/<slug:slug>/", FoodEachDetail.as_view(), name="food-each-detail"),
    path("each/<slug:slug>/update/", FoodEachUpdate.as_view(), name="food-each-update"),
    path(
        "each/<slug:slug>/destroy/", FoodEachDestroy.as_view(), name="food-each-destroy"
    ),
    path("ingredients/", IngredientList.as_view(), name="ingredient-list"),
    path("ingredients/create/", IngredientCreate.as_view(), name="ingredient-create"),
    path(
        "ingredients/<slug:slug>/", IngredientDetail.as_view(), name="ingredient-detail"
    ),
    path(
        "ingredients/<slug:slug>/update/",
        IngredientUpdate.as_view(),
        name="ingredient-update",
    ),
    path(
        "ingredients/<slug:slug>/destroy/",
        IngredientDestroy.as_view(),
        name="ingredient-destroy",
    ),
    path("cooking-methods/", CookingMethodList.as_view(), name="cooking-method-list"),
    path(
        "cooking-methods/create/",
        CookingMethodCreate.as_view(),
        name="cooking-method-create",
    ),
    path(
        "cooking-methods/<slug:slug>/",
        CookingMethodDetail.as_view(),
        name="cooking-method-detail",
    ),
    path(
        "cooking-methods/<slug:slug>/update/",
        CookingMethodUpdate.as_view(),
        name="cooking-method-update",
    ),
    path(
        "cooking-methods/<slug:slug>/destroy/",
        CookingMethodDestroy.as_view(),
        name="cooking-method-destroy",
    ),
]
