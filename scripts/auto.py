from knowledge.models import Knowledge
from general.models import Language, Tag, GenreForURL, Article
from arts.models import Art, Artist, Museum, PaintingMethod, PaintingStyle, ArtsPeriod
from living_things.models import LivingThings, Habitat, Species
from foods.models import Food, CookingMethod, Ingredient
from django.db import connection
from django.contrib.auth.models import User
import json
from accounts.models import UserAccount
from locations.models import Country, Location


def run():
    for choice in Language.NAME_CHOICES:
        Language.objects.create(name=choice[0])

    for choice in GenreForURL.NAME_CHOICES:
        GenreForURL.objects.create(name=choice[0])

    with open("json/general.json") as f:
        general_data = json.load(f)
    article_dict = {
        item["pk"]: item
        for item in general_data
        if item.get("model") == "general.article"
    }

    with open("json/knowledge.json") as f:
        knowledge_data = json.load(f)

    with open("json/locations.json") as f:
        countries_data = json.load(f)

    with open("json/arts.json") as f:
        arts_data = json.load(f)

    with open("json/foods.json") as f:
        foods_data = json.load(f)

    with open("json/living_things.json") as f:
        living_things_data = json.load(f)

    # prefetch common objects
    author = UserAccount.objects.get(pk=1)
    language_en = Language.objects.get(pk=1)
    language_jp = Language.objects.get(pk=2)

    knowledge_list = []
    countries_list = []
    arts_painting_methods_list = []
    arts_painting_style_list = []
    arts_periods_list = []
    living_things_each_list = []
    living_things_habitat_list = []
    living_things_species_list = []
    foods_ingredient_list = []
    foods_cooking_methods_list = []

    articles_for_knowledge_list = []
    articles_for_countries_list = []
    articles_for_arts_painting_methods_list = []
    articles_for_arts_painting_style_list = []
    articles_for_arts_periods_list = []
    articles_for_living_things_each_list = []
    articles_for_living_things_habitat_list = []
    articles_for_living_things_species_list = []
    articles_for_foods_ingredient_list = []
    articles_for_foods_cooking_methods_list = []

    # For Knowledge
    # ====================================================================================================
    for a in reversed(knowledge_data):
        pk_in_json = a["fields"].get("article")
        article_json = article_dict.get(pk_in_json)

        if a["fields"].get("language") == 1:
            language = language_en
        else:
            language = language_jp

        articles_for_knowledge_list.append(
            Article(
                content=article_json["fields"].get("content"),
                kicker=article_json["fields"].get("kicker"),
                excerpt=article_json["fields"].get("excerpt"),
            )
        )

        knowledge_list.append(
            Knowledge(
                name=a["fields"].get("name"),
                slug=a["fields"].get("slug"),
                type="knowledge",
                author=author,
                genre_for_url=GenreForURL.objects.get(name="knowledge"),
                language=language,
                notesite_url=a["fields"].get("notesite_url"),
            )
        )

    articles_for_knowledge_list = Article.objects.bulk_create(
        articles_for_knowledge_list
    )

    for article, knowledge in zip(articles_for_knowledge_list, knowledge_list):
        knowledge.article = article

    Knowledge.objects.bulk_create(knowledge_list)

    # For Country
    # ====================================================================================================

    for a in reversed(countries_data):
        pk_in_json = a["fields"].get("article")
        article_json = article_dict.get(pk_in_json)
        if a["fields"].get("language") == 1:
            language = language_en
        else:
            language = language_jp

        articles_for_countries_list.append(
            Article(
                content=article_json["fields"].get("content"),
                kicker=article_json["fields"].get("kicker"),
                excerpt=article_json["fields"].get("excerpt"),
            )
        )

        countries_list.append(
            Country(
                name=a["fields"].get("name"),
                slug=a["fields"].get("slug"),
                genre_for_url=GenreForURL.objects.get(name="countries"),
                language=language,
            )
        )

    articles_for_countries_list = Article.objects.bulk_create(
        articles_for_countries_list
    )

    for article, country in zip(articles_for_countries_list, countries_list):
        country.article = article

    Country.objects.bulk_create(countries_list)

    # For Arts PaintingMethods
    # ====================================================================================================
    arts_methods_data = [
        item for item in arts_data if item.get("model") == "arts.paintingmethod"
    ]
    print(arts_methods_data)
    for a in reversed(arts_methods_data):
        print(a)
        pk_in_json = a["fields"].get("article")
        article_json = article_dict.get(pk_in_json)
        if a["fields"].get("language") == "en":
            language = language_en
        else:
            language = language_jp

        articles_for_arts_painting_methods_list.append(
            Article(
                content=article_json["fields"].get("content"),
                kicker=article_json["fields"].get("kicker"),
                excerpt=article_json["fields"].get("excerpt"),
            )
        )

        arts_painting_methods_list.append(
            PaintingMethod(
                name=a["fields"].get("name"),
                slug=a["fields"].get("slug"),
                genre_for_url=GenreForURL.objects.get(name="arts/painting-methods"),
                language=language,
            )
        )

    articles_for_arts_painting_methods_list = Article.objects.bulk_create(
        articles_for_arts_painting_methods_list
    )

    for article, painting_methods in zip(
        articles_for_arts_painting_methods_list, arts_painting_methods_list
    ):
        painting_methods.article = article

    PaintingMethod.objects.bulk_create(arts_painting_methods_list)

    # For Arts PaintingStyle
    # ====================================================================================================
    arts_styles_data = [
        item for item in arts_data if item.get("model") == "arts.paintingstyle"
    ]
    for a in reversed(arts_styles_data):
        pk_in_json = a["fields"].get("article")
        article_json = article_dict.get(pk_in_json)
        if a["fields"].get("language") == "en":
            language = language_en
        else:
            language = language_jp

        articles_for_arts_painting_style_list.append(
            Article(
                content=article_json["fields"].get("content"),
                kicker=article_json["fields"].get("kicker"),
                excerpt=article_json["fields"].get("excerpt"),
            )
        )

        arts_painting_style_list.append(
            PaintingStyle(
                name=a["fields"].get("name"),
                slug=a["fields"].get("slug"),
                genre_for_url=GenreForURL.objects.get(name="arts/painting-styles"),
                language=language,
            )
        )

    articles_for_arts_painting_style_list = Article.objects.bulk_create(
        articles_for_arts_painting_style_list
    )

    for article, painting_style in zip(
        articles_for_arts_painting_style_list, arts_painting_style_list
    ):
        painting_style.article = article

    PaintingStyle.objects.bulk_create(arts_painting_style_list)

    # For Arts Periods
    # ====================================================================================================
    arts_periods_data = [
        item for item in arts_data if item.get("model") == "arts.artsperiod"
    ]
    for a in reversed(arts_periods_data):
        pk_in_json = a["fields"].get("article")
        article_json = article_dict.get(pk_in_json)
        if a["fields"].get("language") == "en":
            language = language_en
        else:
            language = language_jp

        articles_for_arts_periods_list.append(
            Article(
                content=article_json["fields"].get("content"),
                kicker=article_json["fields"].get("kicker"),
                excerpt=article_json["fields"].get("excerpt"),
            )
        )

        arts_periods_list.append(
            ArtsPeriod(
                name=a["fields"].get("name"),
                slug=a["fields"].get("slug"),
                genre_for_url=GenreForURL.objects.get(name="arts/periods"),
                language=language,
            )
        )

    articles_for_arts_periods_list = Article.objects.bulk_create(
        articles_for_arts_periods_list
    )
    for article, arts_period in zip(articles_for_arts_periods_list, arts_periods_list):
        arts_period.article = article

    ArtsPeriod.objects.bulk_create(arts_periods_list)

    # For LivingThings Each
    # ====================================================================================================
    living_things_each_data = [
        item
        for item in living_things_data
        if item.get("model") == "living_things.livingthings"
    ]
    for a in living_things_each_data:
        pk_in_json = a["fields"].get("article")
        article_json = article_dict.get(pk_in_json)
        if a["fields"].get("language") == "en":
            language = language_en
        else:
            language = language_jp

        articles_for_living_things_each_list.append(
            Article(
                content=article_json["fields"].get("content"),
                kicker=article_json["fields"].get("kicker"),
                excerpt=article_json["fields"].get("excerpt"),
            )
        )

        living_things_each_list.append(
            LivingThings(
                name=a["fields"].get("name"),
                slug=a["fields"].get("slug"),
                genre_for_url=GenreForURL.objects.get(name="living-things/each"),
                language=language,
            )
        )

    articles_for_living_things_each_list = Article.objects.bulk_create(
        articles_for_living_things_each_list
    )

    for article, living_thing in zip(
        articles_for_living_things_each_list, living_things_each_list
    ):
        living_thing.article = article

    LivingThings.objects.bulk_create(living_things_each_list)

    # For Habitat
    # ====================================================================================================
    habitats_data = [
        item
        for item in living_things_data
        if item.get("model") == "living_things.habitat"
    ]
    for a in habitats_data:
        pk_in_json = a["fields"].get("article")
        print(pk_in_json)
        article_json = article_dict.get(pk_in_json)
        if a["fields"].get("language") == "en":
            language = language_en
        else:
            language = language_jp

        articles_for_living_things_habitat_list.append(
            Article(
                content=article_json["fields"].get("content"),
                kicker=article_json["fields"].get("kicker"),
                excerpt=article_json["fields"].get("excerpt"),
            )
        )

        living_things_habitat_list.append(
            Habitat(
                name=a["fields"].get("name"),
                slug=a["fields"].get("slug"),
                genre_for_url=GenreForURL.objects.get(name="living-things/habitats"),
                language=language,
            )
        )

    articles_for_living_things_habitat_list = Article.objects.bulk_create(
        articles_for_living_things_habitat_list
    )

    for article, habitat in zip(
        articles_for_living_things_habitat_list, living_things_habitat_list
    ):
        habitat.article = article

    Habitat.objects.bulk_create(living_things_habitat_list)

    # For Species
    # ====================================================================================================
    species_data = [
        item
        for item in living_things_data
        if item.get("model") == "living_things.species"
    ]
    for a in species_data:
        pk_in_json = a["fields"].get("article")
        article_json = article_dict.get(pk_in_json)
        if a["fields"].get("language") == "en":
            language = language_en
        else:
            language = language_jp

        articles_for_living_things_species_list.append(
            Article(
                content=article_json["fields"].get("content"),
                kicker=article_json["fields"].get("kicker"),
                excerpt=article_json["fields"].get("excerpt"),
            )
        )

        living_things_species_list.append(
            Species(
                name=a["fields"].get("name"),
                slug=a["fields"].get("slug"),
                genre_for_url=GenreForURL.objects.get(name="living-things/species"),
                language=language,
            )
        )

    articles_for_living_things_species_list = Article.objects.bulk_create(
        articles_for_living_things_species_list
    )

    for article, spec in zip(
        articles_for_living_things_species_list, living_things_species_list
    ):
        spec.article = article

    Species.objects.bulk_create(living_things_species_list)
    # For CookingMethod
    # ====================================================================================================
    foods_cooking_method_data = [
        item for item in foods_data if item.get("model") == "foods.cookingmethod"
    ]
    for a in foods_cooking_method_data:
        pk_in_json = a["fields"].get("article")
        article_json = article_dict.get(pk_in_json)
        if a["fields"].get("language") == "en":
            language = language_en
        else:
            language = language_jp

        articles_for_foods_cooking_methods_list.append(
            Article(
                content=article_json["fields"].get("content"),
                kicker=article_json["fields"].get("kicker"),
                excerpt=article_json["fields"].get("excerpt"),
            )
        )

        foods_cooking_methods_list.append(
            CookingMethod(
                name=a["fields"].get("name"),
                slug=a["fields"].get("slug"),
                genre_for_url=GenreForURL.objects.get(name="foods/cooking-methods"),
                language=language,
            )
        )

    articles_for_foods_cooking_methods_list = Article.objects.bulk_create(
        articles_for_foods_cooking_methods_list
    )

    for article, a in zip(
        articles_for_foods_cooking_methods_list, foods_cooking_methods_list
    ):
        a.article = article

    CookingMethod.objects.bulk_create(foods_cooking_methods_list)
    # For Ingredient
    # ====================================================================================================
    foods_ingredients_data = [
        item for item in foods_data if item.get("model") == "foods.ingredient"
    ]
    for a in foods_ingredients_data:
        pk_in_json = a["fields"].get("article")
        article_json = article_dict.get(pk_in_json)
        if a["fields"].get("language") == "en":
            language = language_en
        else:
            language = language_jp

        articles_for_foods_ingredient_list.append(
            Article(
                content=article_json["fields"].get("content"),
                kicker=article_json["fields"].get("kicker"),
                excerpt=article_json["fields"].get("excerpt"),
            )
        )

        foods_ingredient_list.append(
            Ingredient(
                name=a["fields"].get("name"),
                slug=a["fields"].get("slug"),
                genre_for_url=GenreForURL.objects.get(name="foods/ingredients"),
                language=language,
            )
        )

    articles_for_foods_ingredient_list = Article.objects.bulk_create(
        articles_for_foods_ingredient_list
    )

    for article, ingredient in zip(
        articles_for_foods_ingredient_list, foods_ingredient_list
    ):
        ingredient.article = article

    Ingredient.objects.bulk_create(foods_ingredient_list)
