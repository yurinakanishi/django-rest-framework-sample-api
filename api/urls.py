from django.urls import path, include
from rest_framework.routers import DefaultRouter
from knowledge.views import (
    KnowledgeList,
    KnowledgeDetail,
    KnowledgeCreate,
)

from living_things.views import (
    LivingThingsEachList,
    LivingThingsEachDetail,
    LivingThingsEachCreate,
    LivingThingsHabitatList,
    LivingThingsHabitatDetail,
    LivingThingsHabitatCreate,
    LivingThingsSpecieList,
    LivingThingsSpecieDetail,
    LivingThingsSpecieCreate,
    LivingThingsCountryList,
    LivingThingsCountryDetail,
    LivingThingsCountryCreate,
)

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
    # ArtsPeriodList,
    # ArtsPeriodDetail,
    # ArtsPeriodCreate,
)

from countries.views import (
    CountryList,
    CountryDetail,
    CountryCreate,
)
from movies.views import (
    MovieList,
    MovieDetail,
    MovieCreate,
)

from general.views import (
    GenreList,
    GenreCreate,
    GenreDetail,
    TagList,
    TagCreate,
    TagDetail,
)


urlpatterns = [
    path("knowledge", KnowledgeList.as_view(), name="knowledge-list"),
    path("knowledge/<slug:slug>/", KnowledgeDetail.as_view(), name="knowledge-detail"),
    path(
        "knowledge/<slug:slug>/create",
        KnowledgeCreate.as_view(),
        name="knowledge-create",
    ),
    path(
        "living-things/each",
        LivingThingsEachList.as_view(),
        name="living-things-each-list",
    ),
    path(
        "living-things/each/<slug:slug>/",
        LivingThingsEachDetail.as_view(),
        name="living-things-each-detail",
    ),
    path(
        "living-things/each/<slug:slug>/create",
        LivingThingsEachCreate.as_view(),
        name="living-things-each-create",
    ),
    path(
        "living-things/habitats",
        LivingThingsHabitatList.as_view(),
        name="living-things-habitat-list",
    ),
    path(
        "living-things/habitat/<slug:slug>/",
        LivingThingsHabitatDetail.as_view(),
        name="living-things-habitat-detail",
    ),
    path(
        "living-things/habitat/<slug:slug>/create",
        LivingThingsHabitatCreate.as_view(),
        name="living-things-habitat-create",
    ),
    path(
        "living-things/species",
        LivingThingsSpecieList.as_view(),
        name="living-things-specie-list",
    ),
    path(
        "living-things/species/<slug:slug>/",
        LivingThingsSpecieDetail.as_view(),
        name="living-things-specie-detail",
    ),
    path(
        "living-things/species/<slug:slug>/create",
        LivingThingsSpecieCreate.as_view(),
        name="living-things-specie-create",
    ),
    path(
        "living-things/countries",
        LivingThingsCountryList.as_view(),
        name="living-things-country-list",
    ),
    path(
        "living-things/country/<slug:slug>/",
        LivingThingsCountryDetail.as_view(),
        name="living-things-country-detail",
    ),
    path(
        "living-things/country/<slug:slug>/create",
        LivingThingsCountryCreate.as_view(),
        name="living-things-country-create",
    ),
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
    # path("arts/periods", ArtsPeriodList.as_view(), name="arts-periods-list"),
    # path(
    #     "arts/period/<slug:slug>/",
    #     ArtsPeriodDetail.as_view(),
    #     name="arts-period-detail",
    # ),
    # path(
    #     "arts/period/<slug:slug>/create",
    #     ArtsPeriodCreate.as_view(),
    #     name="arts-period-create",
    # ),
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
    path("movies", MovieList.as_view(), name="movie-list"),
    path("movie/<slug:slug>/", MovieDetail.as_view(), name="movie-detail"),
    path("movie/<slug:slug>/create", MovieCreate.as_view(), name="movie-create"),
    path("countries", CountryList.as_view(), name="country-list"),
    path("country/<slug:slug>/", CountryDetail.as_view(), name="country-detail"),
    path("country/<slug:slug>/create", CountryCreate.as_view(), name="country-create"),
    path("genres", GenreList.as_view(), name="genre-list"),
    path("genre/<slug:name>/", GenreDetail.as_view(), name="genre-detail"),
    path("genre/<slug:name>/create", GenreCreate.as_view(), name="genre-create"),
    path("tags", TagList.as_view(), name="tag-list"),
    path("tag/<slug:name>/", TagDetail.as_view(), name="tag-detail"),
    path("tag/<slug:name>/create", TagCreate.as_view(), name="tag-create"),
]
